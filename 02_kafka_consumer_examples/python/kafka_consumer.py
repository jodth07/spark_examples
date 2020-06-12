"""
@auth jodth07
"""

from datetime import datetime

from kafka import KafkaConsumer


if __name__ == '__main__':

    TOPIC = "topic_one"
    DATE_FORMAT = "%Y-%m-%d %H:%M:%S"
    BOOTSTRAP_SERVERS = ["localhost:9092"]

    consumer = KafkaConsumer(TOPIC,
                             bootstrap_servers=BOOTSTRAP_SERVERS,
                             group_id="twitter-topic_one"
                             )

    for tweet_record in consumer:
        print(tweet_record.value,
              tweet_record.offset,
              datetime.fromtimestamp(tweet_record.timestamp / 1000.).strftime(DATE_FORMAT))
