package com.dimanche.examples;

import org.apache.kafka.clients.producer.KafkaProducer;
import org.apache.kafka.clients.producer.ProducerRecord;
import org.apache.kafka.common.serialization.StringSerializer;

import java.util.Properties;
import static java.lang.Thread.sleep;


public class KafkaProducerExample {

    static KafkaProducer<String, String> getProducer (){
        Properties props = new Properties();
        props.put("bootstrap.servers", "10.0.0.9:9092");
        props.put("acks", "all");
        props.put("retries", 0);
        props.put("batch.size", 16384);
        props.put("linger.ms", 1);
        props.put("buffer.memory", 33554432);
        props.put("key.serializer",   StringSerializer.class.getName());
        props.put("value.serializer", StringSerializer.class.getName());

        return new KafkaProducer<String, String>(props);
    }

    public static void main(String[] args) throws Exception{

        //Assign topicName to string variable
        String topicName = "topic_one";

        KafkaProducer<String, String> producer = getProducer();

        for(int id = 0; id < 10; id++) {
            String data = String.format("{ \"id\": %s, \"link\":\"http://trefle.io/api/subkingdoms/1\", \"name\":\"Tracheobionta\", \"slug\":\"tracheobionta\"}",  Integer.toString(id));

            ProducerRecord<String, String> producerRecord = new ProducerRecord<String, String>(topicName, Integer.toString(id), data);
            producer.send(producerRecord);
            sleep(3000);
        }

        System.out.println("Message sent successfully");
        producer.close();
    }
}