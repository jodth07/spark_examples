"""
spark example reading csv and writing to cassandra,
@auth jodth07
"""

import os
from pyspark.sql import SparkSession
from pyspark.sql.functions import monotonically_increasing_id

spark: SparkSession = SparkSession.builder\
    .master("local[*]") \
    .appName("Cassandra-spark-example") \
    .config("spark.cassandra.connection.host", "127.0.0.1") \
    .getOrCreate()


if __name__ == '__main__':

    os.chdir('../')
    path = os.getcwd() + "/00_input/data/locations.csv"

    # reading csv file with schema, and adding pk
    data = spark\
        .read\
        .options(header='true', inferSchema='true')\
        .csv(f"file://{path}")\
        .withColumn("id", monotonically_increasing_id().astype("int"))

    print(data.columns)

    # writing selected schema to write to cassandra
    cols = ['id', 'location', 'continent', 'population_year', 'population']

    # writing data to cassandra
    data.select(*cols).write\
        .format("org.apache.spark.sql.cassandra")\
        .mode('append')\
        .options(table="populations", keyspace="dev")\
        .save()

    # reading data from cassandra, to confirm write.
    country_data = spark.read\
        .format("org.apache.spark.sql.cassandra")\
        .options(table="populations", keyspace="dev")\
        .load()

    country_data.printSchema()

    country_data.show()
