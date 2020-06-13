"""
spark streaming example writing to cassandra
@auth jodth07
"""
import os

from pyspark.sql.functions import to_timestamp, from_json, col
from pyspark.sql import SparkSession
from cassandra.cluster import Cluster


os.chdir("..")
os.chdir("..")
BASE_DIR = os.getcwd()

INPUT_DIR = os.path.join(BASE_DIR, "00_input", "data")
CHECKPOINT = os.path.join(BASE_DIR, "00_output", "checkpoint")
TOPIC = "topic_one"
BOOTSTRAP_SERVER = "localhost:9092"

cluster = Cluster(['127.0.0.1'])
session = cluster.connect()
session.execute("use dev")

if __name__ == '__main__':

    spark: SparkSession = SparkSession.builder\
        .master("local[*]") \
        .appName("Cassandra-spark-example") \
        .config("spark.cassandra.connection.host", "127.0.0.1") \
        .getOrCreate()

    sample_tweets_df = spark.read\
        .option("inferSchema", True)\
        .option("header", True)\
        .json(f"file://{INPUT_DIR}/tweets.json")

    tweets_schema = sample_tweets_df.schema

    output_df = sample_tweets_df\
        .select("id", "user.name", "user.screen_name", "text", "lang", "source",
                to_timestamp("created_at", "EEE MMM dd HH:mm:ss zzzz yyyy").alias("created_at"))

    output_df.printSchema()

    session.execute("""
    CREATE TABLE IF NOT EXISTS dev.tweets (
        id BIGINT PRIMARY KEY, 
        name TEXT,
        screen_name TEXT,  
        text TEXT,
        lang TEXT, 
        source TEXT, 
        created_at TIMESTAMP)
    """)

    stream_df = spark\
        .readStream \
        .format("kafka") \
        .option("kafka.bootstrap.servers", BOOTSTRAP_SERVER) \
        .option("subscribe", TOPIC) \
        .load()

    tweets_df = stream_df\
        .select(from_json(col("value").cast("string"), tweets_schema))\
        .select("jsontostructs(CAST(value AS STRING)).*")\
        .select("id", "user.name", "user.screen_name", "text", "lang", "source",
                to_timestamp("created_at", "EEE MMM dd HH:mm:ss zzzz yyyy").alias("created_at"))

    streamer = tweets_df.writeStream\
        .option("checkpointLocation", CHECKPOINT)\
        .format("org.apache.spark.sql.cassandra")\
        .option("table", "tweets")\
        .option("keyspace", "dev")\
        .start()

    streamer.awaitTermination()

    cass_data = spark.read\
        .format("org.apache.spark.sql.cassandra")\
        .options(table="tweets", keyspace="dev")\
        .load()

    cass_data.printSchema()
