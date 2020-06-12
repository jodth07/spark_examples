"""
this is an example of receiving twitter streams.
@auth jodth07
"""

import json
from pprint import pprint
from kafka import KafkaConsumer


if __name__ == '__main__':

    BOOTSTRAP_SERVERS = ["localhost:9092"]
    TOPIC = "topic_one"

    consumer = KafkaConsumer(TOPIC,
                             bootstrap_servers=BOOTSTRAP_SERVERS,
                             group_id="counters"
                             )

    for record in consumer:
        pprint(json.loads(str(record.value.decode("utf-8"))))
