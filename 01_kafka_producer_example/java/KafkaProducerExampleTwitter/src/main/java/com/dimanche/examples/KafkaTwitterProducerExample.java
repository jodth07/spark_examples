package com.dimanche.examples;

import org.apache.kafka.clients.producer.KafkaProducer;
import org.apache.kafka.common.serialization.StringSerializer;

import java.util.Properties;

public class KafkaTwitterProducerExample {

    static KafkaProducer<String, String> getProducer (){
        Properties props = new Properties();
        props.put("bootstrap.servers", Constants.BOOTSTRAP_SERVER);
        props.put("acks", "all");
        props.put("retries", Constants.RETRIES);
        props.put("batch.size", Constants.BATCH_SIZE);
        props.put("linger.ms", 1);
        props.put("buffer.memory", Constants.BUFFER_MEMORY);
        props.put("group.id", Constants.GROUP_ID); // default topic name
        props.put("enable.auto.commit", Constants.AUTO_COMMIT);
        props.put("key.serializer",   StringSerializer.class.getName());
        props.put("value.serializer", StringSerializer.class.getName());

        return new KafkaProducer<String, String>(props);
    }

    /*
    public static void main(String[] args) throws Exception{

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
    */
}