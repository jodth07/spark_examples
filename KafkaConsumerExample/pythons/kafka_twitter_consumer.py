import json
from pprint import pprint
from kafka import KafkaConsumer


if __name__ == '__main__':

    TOPIC = "topic_one"

    consumer = KafkaConsumer(TOPIC,
                             bootstrap_servers=["localhost:9092"],
                             group_id="counters"
                             )

    for record in consumer:
        pprint(json.loads(str(record.value.decode("utf-8"))))
