package com.dimanche.examples
import org.apache.log4j.{Level, Logger}
import java.util.Properties
import java.util.Date
import java.text.SimpleDateFormat

import org.apache.kafka.common.serialization.StringSerializer
import org.apache.kafka.clients.producer.{KafkaProducer, ProducerRecord}

object KafkaProducerExample {

  def main(args: Array[String]): Unit = {

    Logger.getLogger("org").setLevel(Level.ERROR)

    val format = new SimpleDateFormat("yyyy-MM-dd HH:mm:ssZ")

    val props = new Properties()
      props.put("bootstrap.servers", "localhost:9092")
      props.put("key.serializer", new StringSerializer().getClass.getName)
      props.put("value.serializer", new StringSerializer().getClass.getName)

    val producer = new KafkaProducer[String, String](props)

    val TOPIC ="topic_one"
    val KEY = TOPIC

    for(i <- 1 to 10) {

      val date = format.format(new Date())
      val value : String =s"""
          |{
          | "time": $date,
          | "data_type":  "Sample",
          | "value": "the current number is $i"
          |}
      """.stripMargin

      val producerRecord = new ProducerRecord(TOPIC, KEY, value)
      producer.send(producerRecord)

      Thread.sleep(1000)

    }

  }

}