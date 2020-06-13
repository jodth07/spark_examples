"""
sample streaming project writing to parquet, as well as writing to
@auth jodth07
"""
import os

from pyspark.sql import SparkSession
from pyspark.sql.functions import from_json, col

if __name__ == '__main__':

    os.chdir("..")
    os.chdir("..")
    BASE_DIR = os.getcwd()
    input_dir = f"file://{BASE_DIR}/00_input/data/"

    TOPIC = "topic_one"
    BOOTSTRAP_SERVER = "localhost:9092"

    spark = SparkSession\
        .builder\
        .appName("StructuredNetworkWordCount")\
        .master("local")\
        .config("spark.jars", f"file://{BASE_DIR}/jars/spark-sql-kafka-0-10_2.11-2.4.4.jar,"
                              f"file://{BASE_DIR}/jars/kafka-clients-2.4.0.jar") \
        .getOrCreate()

    sample_tweets_df = spark.read.json(input_dir + "tweets.json")
    tweets_schema = sample_tweets_df.schema

    tweets_schema.fieldNames()

    stream_df = spark \
        .readStream \
        .format("kafka") \
        .option("subscribe", TOPIC) \
        .option("kafka.bootstrap.servers", BOOTSTRAP_SERVER) \
        .load()

    query_df = stream_df\
        .select(from_json(col("value").cast("string"), tweets_schema))\
        .select("jsontostructs(CAST(value AS STRING)).*")\
        .select("created_at", "id", "lang", "source", "text", "user.name", "user.screen_name")

    query_df.printSchema()

    # Start running the query that prints the running counts to the console
    # console_query = query_df\
    #     .writeStream \
    #     .format("console") \
    #     .start()

    # Start running the query that prints the running counts to the console
    query = query_df \
        .withColumnRenamed("jsontostructs(CAST(value AS STRING))", "value")\
        .writeStream \
        .format("parquet") \
        .option("path", f"file://{BASE_DIR}/00_output/data/tweets")\
        .option("checkpointLocation", f"file://{BASE_DIR}/00_output/data/checkpoints")\
        .start()

    query.awaitTermination()
