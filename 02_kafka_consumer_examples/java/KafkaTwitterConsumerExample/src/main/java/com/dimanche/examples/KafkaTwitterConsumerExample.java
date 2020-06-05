package com.dimanche.examples;

import org.apache.kafka.clients.consumer.*;
import org.apache.kafka.clients.consumer.Consumer;
import org.apache.kafka.common.serialization.LongDeserializer;
import org.apache.kafka.common.serialization.StringDeserializer;

import java.io.BufferedWriter;
import java.io.FileWriter;
import java.io.IOException;
import java.util.ArrayList;
import java.util.Collections;
import java.util.List;
import java.util.Properties;


public class KafkaTwitterConsumerExample {

    private static KafkaConsumer<String, String> createConsumer() {
        final Properties props = new Properties();
        props.put(ConsumerConfig.BOOTSTRAP_SERVERS_CONFIG,     Constants.BOOTSTRAP_SERVER);
        props.put(ConsumerConfig.GROUP_ID_CONFIG,  Constants.GROUP_ID);
        props.put(ConsumerConfig.KEY_DESERIALIZER_CLASS_CONFIG,   StringDeserializer.class.getName());
        props.put(ConsumerConfig.VALUE_DESERIALIZER_CLASS_CONFIG,  StringDeserializer.class.getName());

        return new KafkaConsumer<>(props);
    }

    public static void main(String[] args) throws InterruptedException, IOException {

        final KafkaConsumer<String, String> kafkaConsumer = createConsumer();
        kafkaConsumer.subscribe(Collections.singleton(Constants.TOPIC));

        Constants.TOPICS.add("topic_one");

        kafkaConsumer.subscribe(Constants.TOPICS);

        String data=null;

        while (true){
            try{
                ConsumerRecords<String, String> records = kafkaConsumer.poll(10);
                for (ConsumerRecord<String, String> record: records){

                    System.out.println(String.format("Topic - %s, Partition - %d, \n Value: %s", record.topic(), record.partition(), data));
                }
            }catch (Exception e){
                System.out.println(e.getMessage());
            }
        }

//        kafkaConsumer.close();
//        }
    }
}
