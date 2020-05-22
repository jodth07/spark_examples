from pyspark.sql import SparkSession
from pyspark.sql.functions import explode
from pyspark.sql.functions import split


if __name__ == '__main__':

    spark = SparkSession \
        .builder \
        .appName("StructuredNetworkWordCount") \
        .getOrCreate()

    df = spark \
        .readStream \
        .format("kafka") \
        .option("kafka.bootstrap.servers", "localhost:2181") \
        .option("subscribe", "topic_one") \
        .load()

    df.selectExpr("CAST(key AS STRING)", "CAST(value AS STRING)")