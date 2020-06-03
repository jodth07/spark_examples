package com.dimanche.examples

import org.apache.log4j.{Level, Logger}
import org.apache.spark.SparkContext
import org.apache.spark.sql.SparkSession

object SparkJsonExampleMain {

    def main(args: Array[String]): Unit = {

        val logger = Logger.getLogger("org")
        logger.setLevel(Level.ERROR)

        val spark  = SparkSession.builder()
            .master("local[*]")
            .appName("SparkJsonExample")
            .getOrCreate()

        val sc : SparkContext = spark.sparkContext
        val constants = new ExampleConstants
        val supports = new ExampleSupports(spark)

        import constants.Classes
        import supports._

        for (classification <- Classes){
            val dataDF  = spark.read.json(getInputPath(classification))
            dataDF.printSchema()
            outputToJSon(dataDF, classification)
        }

      spark.stop()
    }
}
