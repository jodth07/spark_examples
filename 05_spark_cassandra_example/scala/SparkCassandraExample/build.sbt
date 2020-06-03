name := "SparkCassandraExample"

version := "0.1"

scalaVersion := "2.11.8"


libraryDependencies ++= Seq(
  "org.apache.spark" %% "spark-core" % "2.4.4",
  "org.apache.spark" %% "spark-sql" % "2.4.4",
  "org.apache.spark" %% "spark-hive" % "2.4.4",
  "org.apache.spark" %% "spark-yarn" % "2.4.4",
  "org.scalatest" %% "scalatest" % "3.0.8"
)

libraryDependencies += "com.datastax.spark" % "spark-cassandra-connector_2.11" % "2.5.0"
