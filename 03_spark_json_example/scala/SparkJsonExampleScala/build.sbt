name := "SparkJsonExample"

version := "0.1"

scalaVersion := "2.11.8"

libraryDependencies ++= Seq(
  "org.apache.spark" %% "spark-core" % "2.4.4",
  "org.apache.spark" %% "spark-sql" % "2.4.4",
  "org.apache.spark" %% "spark-hive" % "2.4.4",
  "org.apache.spark" %% "spark-yarn" % "2.4.4",
//  "org.apache.hadoop" %% "hadoop-common" % "2.7.3",
  "org.scalatest" %% "scalatest" % "3.0.8"
)

// https://mvnrepository.com/artifact/org.apache.hadoop/hadoop-common
libraryDependencies += "org.apache.hadoop" % "hadoop-common" % "2.7.3"
