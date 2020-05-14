package dimanche.json.examples

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

    //    val data_df = spark.read.json(Json)
    val sc : SparkContext = spark.sparkContext
    val constants = new ExampleConstants
    val supports = new ExampleSupports(spark)
    import constants._
    import supports._


    val subData  = spark.read.json(getInputPath(Subkingdom))
    subData.printSchema()
    outputToJSon(subData, Subkingdom)

    val kingData  = spark.read.json(Kingdom)
    kingData.printSchema()
    outputToJSon(kingData, Kingdom)

    val divData  = spark.read.json(Division)
    divData.printSchema()
    outputToJSon(divData, Division)

    val famData  = spark.read.json(Family)
    famData.printSchema()
    outputToJSon(famData, Family)

    val genusData  = spark.read.json(Genus)
    genusData.printSchema()
    outputToJSon(genusData, Genus)

    val plantData  = spark.read.json(Plant)
    plantData.printSchema()
    outputToJSon(plantData, Plant)

    spark.stop()
  }
}
