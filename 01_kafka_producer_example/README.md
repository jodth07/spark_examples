## Start Kafka

### run setup.sh to start kafka

#### start zookeeper
> zookeeper-server-start.sh $KAFKA_HOME/config/zookeeper.properties

#### start kafka server(s)
> kafka-server-start.sh $KAFKA_HOME/config/server.properties

#### create topic with replication and partition
> kafka-topics.sh --bootstrap-server localhost:9092 --topic topic_one --create --replication-factor 1 --partitions 1 

#### get topic(s) information
> kafka-topics.sh --bootstrap-server localhost:9092 --describe

#### start console producer
> kafka-console-producer.sh --bootstrap-server localhost:9092 --topic topic_one

#### Start console consumer
> kafka-console-consumer.sh --bootstrap-server localhost:9092 --topic topic_one --from-beginning

