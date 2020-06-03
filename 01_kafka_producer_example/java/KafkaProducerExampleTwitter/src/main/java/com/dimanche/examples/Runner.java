package com.dimanche.examples;

import org.apache.kafka.clients.producer.KafkaProducer;
import org.apache.kafka.clients.producer.ProducerRecord;

import twitter4j.FilterQuery;
import twitter4j.Status;
import twitter4j.StatusListener;
import twitter4j.TwitterStream;

import java.util.concurrent.LinkedBlockingQueue;
import static java.lang.Thread.sleep;

import static com.dimanche.examples.KafkaTwitterProducerExample.getProducer;
import static com.dimanche.examples.TwitterStreamer.getListener;
import static com.dimanche.examples.TwitterStreamer.getStreamer;

public class Runner {
    public static void main(String[] args) throws Exception {

        String[] keyWords = {"nentindo", "switch", "switches"};
        final LinkedBlockingQueue<Status> queue = new LinkedBlockingQueue<Status>(1000);
        String topicName = "topic_one";

        TwitterStream twitterStream = getStreamer();
        StatusListener listener = getListener(queue);
        twitterStream.addListener(listener);

        FilterQuery query = new FilterQuery().track(keyWords);
        twitterStream.filter(query);

        KafkaProducer<String, String> producer = getProducer();


        int i = 0;

        while (i < 10) {
            Status ret = queue.poll();

            if (ret == null) {
                Thread.sleep(100);
                i++;
            } else {

                Status tweet = queue.take();
                long id = tweet.getId();

                System.out.println(tweet.toString());

                ProducerRecord<String, String> producerRecord = new ProducerRecord<String, String>(topicName, Long.toString(id), tweet.toString());
                producer.send(producerRecord);
            }
        }

        System.out.println("Message sent successfully");

        sleep(5000);
        producer.close();
        twitterStream.shutdown();
    }
}