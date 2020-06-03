from pyspark.sql.functions import monotonically_increasing_id
from pyspark.sql import SparkSession
import os

spark: SparkSession = SparkSession.builder\
    .master("local[*]") \
    .appName( "Cassandra-spark-example") \
    .config("spark.cassandra.connection.host", "127.0.0.1") \
    .getOrCreate()


if __name__ == '__main__':

    os.chdir('../')
    path = os.getcwd() + "/inputdata/locations.csv"

    data = spark\
        .read\
        .options(header='true', inferSchema='true')\
        .csv(f"file://{path}")\
        .withColumn("id", monotonically_increasing_id().astype("int"))

    print(data.columns)

    cols = ['id', 'location', 'continent', 'population_year', 'population']
    data.select(*cols).write\
        .format("org.apache.spark.sql.cassandra")\
        .mode('append')\
        .options(table="populations", keyspace="dev")\
        .save()

    country_data = spark.read\
        .format("org.apache.spark.sql.cassandra")\
        .options(table="populations", keyspace="dev")\
        .load()

    country_data.printSchema()

    country_data.show()
