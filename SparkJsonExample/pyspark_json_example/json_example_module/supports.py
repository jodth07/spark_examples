from pyspark.sql import SparkSession
from pyspark.sql import DataFrame
import os


class ExampleSupport():
    os.chdir("../..")
    base_dir = os.getcwd()

    def __init__(self, spark_session : SparkSession, base_path : str = None):
        self.spark = spark_session
        self.base_dir : str = base_path if base_path else f"file://{os.getcwd()}"

    def get_input_path(self, name : str) -> str :
        return f"{self.base_dir}/inputdata/{name}.json"

    def get_output_path(self, name : str) -> str :
        return f"{self.base_dir}/outputdata/{name}.json"

    def output_to_json(self, df: DataFrame, endpoint : str) -> bool:
        df.coalesce(1).write.json(self.get_output_path(endpoint))
        return True
