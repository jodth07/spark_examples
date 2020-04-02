from pyspark.sql import SparkSession
from pyspark.sql import DataFrame

class ExampleSupport():
    def __init__(self, sparkSession : SparkSession, base_path : str = None):
        self.spark = sparkSession
        self.BASEPATH : str = base_path if base_path else "file:///home/yashiro/Desktop/spark_examples"

    def get_input_path(self, name : str) -> str :
        return f"{self.BASEPATH}/inputdata/{name}.json"
    

    def get_output_path(self, name : str) -> str :
        return f"{self.BASEPATH}/outputdata/{name}.json"
    

    def output_to_json(self, df: DataFrame, endpoint : str) -> bool:
        df.coalesce(1).write.json(self.get_output_path(endpoint))
        return True