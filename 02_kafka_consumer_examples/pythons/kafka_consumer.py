from kafka import KafkaConsumer
from datetime import datetime


if __name__ == '__main__':

    TOPIC = "topic_one"
    fmt = "%Y-%m-%d %H:%M:%S"

    consumer = KafkaConsumer(TOPIC,
                             bootstrap_servers=["localhost:9092"],
                             group_id="counters"
                             )

    for record in consumer:
        print(record.value,
              record.offset,
              datetime.fromtimestamp(record.timestamp / 1000.).strftime(fmt))
