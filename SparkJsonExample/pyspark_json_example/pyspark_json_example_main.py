from pyspark.sql import SparkSession
from pyspark.sql import DataFrame
from json_example_module import *
from json_example_module.supports import ExampleSupport


if __name__ == '__main__':

    spark = SparkSession\
        .Builder()\
        .appName("pyspark_json_example")\
        .master("local")\
        .getOrCreate()

    support : ExampleSupport = ExampleSupport(spark)

    subData : DataFrame = spark.read.json(support.get_input_path(SUBKINGDOM))
    subData.printSchema()
    support.output_to_json(subData, support.get_output_path(SUBKINGDOM))


    print("Hello World")
    print(SUBKINGDOM)

