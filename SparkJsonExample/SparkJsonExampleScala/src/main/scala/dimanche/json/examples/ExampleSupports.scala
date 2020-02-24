package dimanche.json.examples
import org.apache.spark.sql.{DataFrame, SparkSession}

class ExampleSupports(sparkSession: SparkSession) {

  val BasePath : String = "file:///home/yashiro/Desktop/spark_examples/"

  def getInputPath(name : String): String = {
    f"${BasePath}/inputdata/${name}.json"
  }

  def getOutputPath(name : String): String = {
    f"${BasePath}/outputdata/${name}.json"
  }

  def outputToJSon(df: DataFrame, endpoint : String, sparkSession: SparkSession = sparkSession ): Unit ={
    df.coalesce(1).write.json(getOutputPath(endpoint))
  }
}
