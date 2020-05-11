name := "SparkHbaseBatchExample"

version := "0.1"

scalaVersion := "2.11.8"

// https://mvnrepository.com/artifact/org.apache.spark/spark-core
libraryDependencies += "org.apache.spark" %% "spark-core" % "2.4.4"

// https://mvnrepository.com/artifact/org.apache.spark/spark-core
libraryDependencies += "org.apache.spark" %% "spark-sql" % "2.4.4"
libraryDependencies += "org.apache.spark" %% "spark-streaming" % "2.4.4"

libraryDependencies += "log4j" % "log4j" % "1.2.17"

// https://mvnrepository.com/artifact/org.apache.hbase/hbase-client
libraryDependencies += "org.apache.hbase" % "hbase-client" % "2.2.3"
libraryDependencies += "org.apache.hbase" % "hbase-common" % "2.2.3"
//libraryDependencies += "org.apache.hbase" % "hbase-spark" % "2.0.0"
// https://mvnrepository.com/artifact/org.apache.hbase/hbase-spark
libraryDependencies += "org.apache.hbase" % "hbase-spark" % "2.1.0-cdh6.3.3"

// https://mvnrepository.com/artifact/com.hortonworks/shc-core
//libraryDependencies += "com.hortonworks" % "shc-core" % "1.1.1-2.1-s_2.11"


resolvers ++= Seq(
  "Apache Repository" at "https://repository.apache.org/content/repositories/releases/"
)