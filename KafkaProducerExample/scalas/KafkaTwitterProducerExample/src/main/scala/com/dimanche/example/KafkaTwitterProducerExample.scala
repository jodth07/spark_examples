package com.dimanche.examples

import com.dimanche.example.TwitterStream
import com.dimanche.example.TwitterStream.OnTweetPosted

import org.apache.log4j.{Level, Logger}
import java.util.Properties

import twitter4j._
import org.apache.kafka.common.serialization.StringSerializer
import org.apache.kafka.clients.producer.{KafkaProducer, ProducerRecord}

object KafkaTwitterProducerExample{
  val TOPIC : String  = "topic_one"
  val KEY : String = TOPIC

  val props : Properties = new Properties()
  props.put("bootstrap.servers", "localhost:9092")
  props.put("key.serializer", new StringSerializer().getClass.getName)
  props.put("value.serializer", new StringSerializer().getClass.getName)

  val producer = new KafkaProducer[String, String](props)

  def main(args: Array[String]): Unit = {

    val filters = new FilterQuery().track("trump")

    val twitterStream = TwitterStream.getStream
    twitterStream.addListener(new OnTweetPosted(status => sendToKafka(status)))
    twitterStream.filter(filters)

  }

  def sendToKafka(tweet: Status): Unit ={
//    println(tweet.getText)
    val producerRecord = new ProducerRecord[String, String](
      TOPIC,
      tweet.getUser.getScreenName,
      TwitterObjectFactory.getRawJSON(tweet)
    )
    producer.send(producerRecord)
  }

}