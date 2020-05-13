#!/bin/bash
# Start kafka

zookeeper-server-start.sh -daemon $KAFKA_HOME/config/zookeeper.properties
sleep 3

kafka-server-start.sh -daemon $KAFKA_HOME/config/server.properties
sleep 3

kafka-topics.sh --zookeeper localhost:2181 --create  --replication-factor 1 --partitions 1 --topic topic_one
sleep 1
