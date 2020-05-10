package com.dimanche.examples
import com.datastax.spark.connector._
import org.apache.spark.sql.cassandra._

import org.apache.log4j.{Level, Logger}
import org.apache.spark.SparkContext
import org.apache.spark.SparkConf
import org.apache.spark.sql.SparkSession


object SparkCassandraExample {

  def main(args: Array[String]): Unit = {

    val logger = Logger.getLogger("org")
    logger.setLevel(Level.ERROR)

    val conf = new SparkConf().setAppName("Cassandra Example").setMaster("local[*]")

    val spark  = SparkSession.builder()
      .config(conf)
      .getOrCreate()

    val sc = spark.sparkContext
    
    println("Hello World")

  }

}