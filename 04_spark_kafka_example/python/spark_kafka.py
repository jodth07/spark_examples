"""
spark streaming example, writing to console from kafka
@auth jodth07
"""

import os
from pyspark.sql import SparkSession


os.chdir("..")
os.chdir("..")
BASE_PATH = os.getcwd()

TOPIC = "topic_one"
BOOTSTRAP_SERVER = "localhost:9092"


if __name__ == '__main__':
    print("PySpark Structured Streaming with Kafka")

    spark = SparkSession\
        .builder\
        .appName("StructuredNetworkWordCount")\
        .master("local")\
        .config("spark.jars",
                f"file://{BASE_PATH}/jars/spark-sql-kafka-0-10_2.11-2.4.4.jar,"
                f"file://{BASE_PATH}/jars/kafka-clients-2.4.0.jar") \
        .getOrCreate()

    stream_df = spark\
        .readStream \
        .format("kafka") \
        .option("kafka.bootstrap.servers", BOOTSTRAP_SERVER) \
        .option("subscribe", TOPIC) \
        .load()

    string_df = stream_df.selectExpr("CAST(value AS STRING)")

    # Start running the query that prints the running counts to the console
    query = string_df \
        .writeStream \
        .format("console") \
        .start()

    query.awaitTermination()
