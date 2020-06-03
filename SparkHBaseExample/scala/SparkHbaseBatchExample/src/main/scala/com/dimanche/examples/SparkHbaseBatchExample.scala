package com.dimanche.examples

import org.apache.log4j.{Level, Logger}
import org.apache.spark.sql.SparkSession
import org.apache.hadoop.hbase.spark.datasources.HBaseTableCatalog


object SparkHbaseBatchExample {

  val appName : String = "Spark Hbase"
  val master : String = "local"

  def main(args: Array[String]): Unit = {
    //  Spark and logger  Configurations
    Logger.getLogger("org").setLevel(Level.ERROR)

    val spark : SparkSession = SparkSession.
      builder().
      appName(appName).
      master(master).
      getOrCreate()
    import spark.implicits._

    case class Employee(key: String, fName: String, lName: String,
                        mName:String, addressLine:String, city:String,
                        state:String, zipCode:String)

    val data = Seq(Employee("1","Abby","Smith","K","3456 main", "Orlando","FL","45235"),
      Employee("2","Amaya","Williams","L","123 Orange","Newark", "NJ", "27656"),
      Employee("3","Alchemy","Davis","P","Warners","Sanjose","CA", "34789"))

    val df = spark.sparkContext.parallelize(data).toDF

    def catalog =
      s"""{
         |"table":{"namespace":"default", "name":"employee"},
         |"rowkey":"key",
         |"columns":{
         |"key":{"cf":"rowkey", "col":"key", "type":"string"},
         |"fName":{"cf":"person", "col":"firstName", "type":"string"},
         |"lName":{"cf":"person", "col":"lastName", "type":"string"},
         |"mName":{"cf":"person", "col":"middleName", "type":"string"},
         |"addressLine":{"cf":"address", "col":"addressLine", "type":"string"},
         |"city":{"cf":"address", "col":"city", "type":"string"},
         |"state":{"cf":"address", "col":"state", "type":"string"},
         |"zipCode":{"cf":"address", "col":"zipCode", "type":"string"}
         |}
         |}""".stripMargin

    df.write.options(
      Map(HBaseTableCatalog.tableCatalog -> catalog, HBaseTableCatalog.newTable -> "4"))
      .format("org.apache.spark.sql.execution.datasources.hbase")
      .save()

  }
}