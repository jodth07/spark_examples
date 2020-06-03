package com.dimanche.examples

import org.apache.spark.sql.{DataFrame, SparkSession}
import java.io.File

class ExampleSupports(sparkSession: SparkSession) {

  val CPath = new File("../../..").getCanonicalPath
  val BasePath : String = s"file://${CPath}/"

  def getInputPath(name : String): String = {
      f"${BasePath}/00_input/data/${name}.json"
  }

  def getOutputPath(name : String): String = {
      f"${BasePath}/00_output/data/${name}"
  }

  def outputToJSon(df: DataFrame, endpoint : String, sparkSession: SparkSession = sparkSession ): Unit ={
      df.coalesce(1).write.json(getOutputPath(endpoint))
  }
}

