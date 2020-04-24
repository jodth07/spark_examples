package com.dimanche.examples
import java.nio.file.Paths
import org.apache.hadoop.hbase.protobuf.generated.TableProtos.TableName
import org.apache.spark.sql.SparkSession
import org.apache.log4j.{Level, Logger}
//import org.apache.hadoop.hbase.spark.datasources.HBaseTableCatalog

//import org.apache.hadoop.
import org.apache.hadoop.hbase.client.{Connection, ConnectionFactory, Put}

import org.apache.hadoop.hbase.util.ByteStringer

object SparkHbaseBatchExample {

  val appName : String = "Spark Hbase"
  val master : String = "local"

  def main(args: Array[String]): Unit = {

    Logger.getLogger("org").setLevel(Level.ERROR)

    val spark : SparkSession = SparkSession.
      builder().
      appName(appName).
      master(master).
      getOrCreate()

//    val HbaseConf =

    val currentPath = Paths.get(System.getProperty("user.dir"))
    val baseBath = currentPath.getParent().getParent().getParent()
    val genusesPath = Paths.get(baseBath.toString, "_inputdata", "genuses.json")

    val genusesDF = spark.read.json(s"file://${genusesPath}")
    genusesDF.printSchema()

    val tableName = "genuses"
//    val table = TableName.valueOf(tableName)
    val ddl : String = "create 'genuses' 'main', 'class', 'division', 'family', 'kingdom', 'order', 'subkingdom'"

//  Table genuses
//  Column families : main, class, division, family, kingdom, name, order, subkingdom
//  Key id


  }
}