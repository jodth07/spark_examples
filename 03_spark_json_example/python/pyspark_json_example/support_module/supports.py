"""
Support class for reading and writing data,
as well as constants to be used in the classes
@auth jodth07
"""

import os
from pyspark.sql import DataFrame


class ExampleSupport:
    """
    Support class to get data paths and to write to output directory.
    """
    os.chdir("../../..")
    base = os.getcwd()

    def __init__(self, base_path: str = None):
        """
        this path should be set if working with this module as a standalone
        :param base_path: base path to be set based on personal location.
        if not set, the base path is set to the location of the main outer package spark_examples
        """
        self.base_dir: str = base_path if base_path else f"file://{self.base}"

    def get_input_path(self, name: str) -> str:
        """
        this gets input path for json, csv, and other files
        :param name: string to be used get data based on name
        """
        return f"{self.base_dir}/00_input/data/{name}*"

    def get_output_path(self, name: str) -> str:
        """
        string to be used create full writing path based on name
        :param name: use name to create realpath
        """
        return f"{self.base_dir}/00_output/data/{name}"

    def output_to_json(self, dataframe: DataFrame, endpoint: str) -> bool:
        """
        write json file to output path
        :param dataframe: spark dataframe to be used for to write data
        :param endpoint: api endpoint used to gather the data as
        well as to create path to write the data to
        """
        dataframe.coalesce(1).write.json(self.get_output_path(endpoint))
        return True


class ExampleConstants:
    """
    This class sets up enums for the classifications hierarchy,
    which is used as both storage path and api endpoints.
    """
    SUBKINGDOM: str = "subkingdoms"
    KINGDOM: str = "kingdoms"
    DIVISION: str = "divisions"
    FAMILY: str = "families"
    GENUS: str = "genuses"
    PLANT: str = "plants"

    CLASSES: list = [SUBKINGDOM, KINGDOM, DIVISION, FAMILY, GENUS, PLANT]
