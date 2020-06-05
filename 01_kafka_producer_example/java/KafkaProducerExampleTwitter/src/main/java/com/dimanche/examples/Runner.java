package com.dimanche.examples;


import org.apache.kafka.clients.producer.KafkaProducer;
import org.apache.kafka.clients.producer.ProducerRecord;

import twitter4j.*;

import java.util.concurrent.LinkedBlockingQueue;
import java.util.regex.Matcher;
import java.util.regex.Pattern;

import static java.lang.Thread.sleep;

import static com.dimanche.examples.KafkaTwitterProducerExample.getProducer;
import static com.dimanche.examples.TwitterStreamer.getListener;
import static com.dimanche.examples.TwitterStreamer.getStreamer;

public class Runner {
    public static void main(String[] args) throws Exception {

        String[] keyWords = {"nentindo", "switch", "switches", "trump"};
        final LinkedBlockingQueue<String> queue = new LinkedBlockingQueue<String>(1000);
        String topicName = "topic_one";

        TwitterStream twitterStream = getStreamer();
        StatusListener listener = getListener(queue);
        twitterStream.addListener(listener);

        FilterQuery query = new FilterQuery().track(keyWords);
        twitterStream.filter(query);

        KafkaProducer<String, String> producer = getProducer();

        int i = 0;

        while (i < 10) {
            String ret = queue.poll();

            if (ret == null) {
                Thread.sleep(100);
                i++;
            } else {

                String tweet = queue.take();

                System.out.println(tweet);

                ProducerRecord<String, String> producerRecord = new ProducerRecord<String, String>(topicName, "id", tweet);
                producer.send(producerRecord);
            }
        }

        System.out.println("Message sent successfully");

        sleep(5000);
        producer.close();
        twitterStream.shutdown();
    }
}