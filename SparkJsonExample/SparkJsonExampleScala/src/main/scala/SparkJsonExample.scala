import org.apache.spark.SPARK_VERSION
import org.apache.spark.SparkContext
import org.apache.spark.sql.SparkSession
import org.apache.log4j.{Level, Logger}

object SparkJsonExample {

  def getPath(name : String): String = {
    val BasePath : String = "file:///Users/speedy/Desktop/spark_connect_examples/inputdata"
    f"${BasePath}/${name}.json"
  }

  def main(args: Array[String]): Unit = {
    val logger = Logger.getLogger("org")
    logger.setLevel(Level.ERROR)

    val spark  = SparkSession.builder()
      .master("local[*]")
      .appName("SparkJsonExample")
      .getOrCreate()

    val SubkingdomPath : String = getPath("subkingdoms")
    val KingdomPath : String = getPath("kingdoms")
    val DivisionPath : String = getPath("divisions")
    val GenusPath : String = getPath("genuses")
    val PlantPath : String = getPath("plants")


    //    val data_df = spark.read.json(JsonPath)
    val sc : SparkContext = spark.sparkContext
    val subData  = spark.read.json(SubkingdomPath)
    subData.printSchema()

    val kingData  = spark.read.json(KingdomPath)
    kingData.printSchema()

    val divData  = spark.read.json(DivisionPath)
    divData.printSchema()

    val genusData  = spark.read.json(GenusPath)
    genusData.printSchema()

    val plantData  = spark.read.json(PlantPath)
    plantData.printSchema()

  }

}
