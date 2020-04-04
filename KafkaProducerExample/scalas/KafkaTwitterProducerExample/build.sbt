name := "KafkaTwitterProducerExample"

version := "0.1"

scalaVersion := "2.11.8"

libraryDependencies +=  "org.apache.kafka" %% "kafka" % "2.4.0"
libraryDependencies += "log4j" % "log4j" % "1.2.17"
// https://mvnrepository.com/artifact/org.twitter4j/twitter4j-core
libraryDependencies += "org.twitter4j" % "twitter4j-core" % "4.0.4"
libraryDependencies += "org.twitter4j" % "twitter4j-stream" % "4.0.4"
