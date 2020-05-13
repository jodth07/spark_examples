package com.dimanche.examples


import org.apache.log4j.{Level, Logger}

import java.util.Properties
import java.util.Collections.singletonList

import org.apache.kafka.common.serialization.StringDeserializer
import org.apache.kafka.clients.consumer.{ConsumerRecords, KafkaConsumer}

object KafkaConsumerExample {

  val TOPIC : String  = "topic_one"

  val props : Properties = new Properties()
  props.put("bootstrap.servers", "localhost:9092")
  props.put ("auto.offset.reset", "latest" )
  props.put ("group.id", "topic_one" )
  props.put("key.deserializer", new StringDeserializer().getClass.getName)
  props.put("value.deserializer", new StringDeserializer().getClass.getName)


  def main(args: Array[String]): Unit = {

    val kafkaConsumer = new KafkaConsumer[String, String](props)

    kafkaConsumer.subscribe(singletonList(TOPIC))

    while(true){

      val records : ConsumerRecords[String,String] = kafkaConsumer.poll(2000)// poll is currently deprecated
      val recordsIter = records.iterator()

      while (recordsIter.hasNext){
        val record = recordsIter.next
        println(s"${record.offset()} \t ${record.value()}")
      }

    }
  }
}
