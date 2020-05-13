## Start Kafka

### run setup.sh to start kafka

start console producer
> kafka-console-producer.sh --bootstrap-server localhost:9092 --topic topic_one

Start console consumer
> kafka-console-consumer.sh --bootstrap-server localhost:9092 --topic topic_one --from-beginning

