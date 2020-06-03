package com.dimanche.examples

import spray.json._
import DefaultJsonProtocol._

import java.util.Properties
import java.util.Collections.singletonList

import org.apache.kafka.common.serialization.StringDeserializer
import org.apache.kafka.clients.consumer.{ConsumerRecords, KafkaConsumer}

object KafkaTwitterConsumerExample {

    val TOPIC : String  = "topic_one"

    val props : Properties = new Properties()
    props.put("bootstrap.servers", "localhost:9092")
    props.put ("auto.offset.reset", "earliest" )
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
                val currentOffset = record.offset()
                println(currentOffset)
                try {
                    val jsRecord = record.value().parseJson.asJsObject()
                    val data = (jsRecord.getFields("user"),jsRecord.getFields("lang"),
                      jsRecord.getFields("id"),jsRecord.getFields("text"),
                      jsRecord.getFields("created_at"))
                    println(currentOffset, data)
                } finally {
                    println("finally")
                }
            }
        }
    }
}
