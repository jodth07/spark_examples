"""
pyspark write to hive example
@auth jodth07
"""
import os

from pyspark.sql import SparkSession
from pyspark.sql.functions import to_date, col


os.chdir("../..")
BASE_DIR: str = os.getcwd()
INPUT_DIR: str = os.path.join(BASE_DIR, "00_input", "data")
SPARK_WAREHOUSE: str = "spark-warehouse"

if __name__ == '__main__':
    spark = SparkSession\
        .builder\
        .master("local[*]")\
        .appName("spark_hive_example") \
        .config("spark.sql.warehouse.dir", SPARK_WAREHOUSE)\
        .config("hive.exec.dynamic.partition.mode", True)\
        .config("hive.exec.dynamic.partition.mode", "nonstrict")\
        .enableHiveSupport()\
        .getOrCreate()

    spark.sql("""
        DROP TABLE IF EXISTS products.orders
    """)

    spark.sql("""
        DROP DATABASE IF EXISTS products
    """)


    spark.sql("""
        CREATE DATABASE IF NOT EXISTS products
        LOCATION "/user/yashiro/products"
    """)

    spark.sql("""
        CREATE TABLE IF NOT EXISTS products.orders(
            OrderNum INT,
            CustNum BIGINT,
            ProductID STRING,
            Quantity INT
        )
        PARTITIONED BY (purchasedate DATE)
    """)

    spark.sql("DESCRIBE FORMATTED products.orders").show(truncate=False)

    orders_df = spark.read\
        .option("header", True)\
        .option("inferSchema", True)\
        .csv(f"file://{INPUT_DIR}/orders.csv")

    # orders_df.show()
    df = orders_df.withColumn("purchasedate", to_date(col("Date of Purchase"), "m/d/yyyy"))\
        .drop("Date of Purchase")

    print(df.count())
    clean_df = df.na.drop(subset="purchasedate")

    print(clean_df.count())
    clean_df.show()
    clean_df.coalesce(1).write.mode("overwrite").insertInto("products.orders")
