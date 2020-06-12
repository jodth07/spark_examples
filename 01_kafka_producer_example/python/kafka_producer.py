"""
@auth jodth07
"""

from time import sleep
from json import dumps
from datetime import datetime

from kafka import KafkaProducer


def send_message(topic: str, producer: KafkaProducer) -> bool:
    """
    send randomly generated data through kafka
    :param topic: topic to send the messages through
    :param producer: kafka producer used to send the message
    """
    for counter in range(10):
        data = {
            "time": str(datetime.now()),
            "data_type": "Sample",
            'value': f"the current number is {counter}"
        }
        producer.send(topic, value=data)
        sleep(2)
    return True


if __name__ == '__main__':
    TOPIC = "topic_one"
    BOOTSTRAP_SERVERS = ['localhost:9092']

    kafka_producer = KafkaProducer(bootstrap_servers=BOOTSTRAP_SERVERS,
                                   value_serializer=lambda record: dumps(record).encode('utf-8'))

    send_message(TOPIC, kafka_producer)
