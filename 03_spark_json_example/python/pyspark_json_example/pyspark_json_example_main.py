from pyspark.sql import SparkSession
from pyspark.sql import DataFrame

from support_module.supports import ExampleSupport
from support_module.supports import ExampleConstants


if __name__ == '__main__':

    spark = SparkSession\
        .Builder()\
        .appName("pyspark_json_example")\
        .master("local")\
        .getOrCreate()

    support: ExampleSupport = ExampleSupport()
    constants = ExampleConstants()

    for data_class in constants.CLASSES:
        data: DataFrame = spark.read.json(support.get_input_path(data_class))
        data.printSchema()
        support.output_to_json(data, support.get_output_path(data_class))


