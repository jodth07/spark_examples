from pyspark.sql import DataFrame
import os


class ExampleSupport:
    os.chdir("../../..")
    base = os.getcwd()

    def __init__(self, base_path: str = None):
        self.base_dir : str = base_path if base_path else f"file://{self.base}"

    def get_input_path(self, name: str) -> str:
        return f"{self.base_dir}/00_input/data/{name}.json"

    def get_output_path(self, name: str) -> str:
        return f"{self.base_dir}/00_output/data/{name}"

    def output_to_json(self, df: DataFrame, endpoint: str) -> bool:
        df.coalesce(1).write.json(self.get_output_path(endpoint))
        return True


class ExampleConstants:
    """
    description tbd
    """
    SUBKINGDOM: str = "subkingdoms"
    KINGDOM: str = "kingdoms"
    DIVISION: str = "divisions"
    FAMILY: str = "families"
    GENUS: str = "genuses"
    PLANT: str = "plants"

    CLASSES: list = [SUBKINGDOM, KINGDOM, DIVISION, FAMILY, GENUS, PLANT]
