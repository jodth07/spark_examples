from pyspark import SparkConf
from pyspark.sql import SparkSession


BASE_PATH : str = "/inputdata"


def get_path(name:str, base_path:str = BASE_PATH):
    return f"{base_path}/{name}.json"


if __name__ == '__main__':
    app_name = "spark_json_example"
    spark = SparkSession\
        .Builder()\
        .appName(app_name)\
        .master("local[*]")\
        .getOrCreate()

    print(get_path(
        "families"
    ))