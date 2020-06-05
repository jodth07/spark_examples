package com.dimanche.examples;

import java.util.ArrayList;

public class Constants {
    static final String BOOTSTRAP_SERVER = "localhost:9092";
    static final String GROUP_ID = "KafkaExampleConsumer";
    static final String TOPIC = "topic_one";
    static final ArrayList<String> TOPICS = new ArrayList<String>();


    public static Integer MESSAGE_COUNT=1000;
    public static String CLIENT_ID="client1";
    public static String GROUP_ID_CONFIG="consumerGroup1";
    public static Integer MAX_NO_MESSAGE_FOUND_COUNT=100;
    public static String OFFSET_RESET_LATEST="latest";
    public static String OFFSET_RESET_EARLIER="earliest";
    public static Integer MAX_POLL_RECORDS=1;

}
