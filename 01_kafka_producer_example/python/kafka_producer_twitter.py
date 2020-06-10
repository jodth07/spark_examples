"""
Kafka twitter producer example using python-kafka
@auth: jodth07
"""
import os

# # # # # Twitter API Libraries # # # #
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream

# # # # # KAFKA Libraries # # # #
from kafka import KafkaProducer


class Listener(StreamListener):
    """
    This is a basic listener that just prints received tweets to stdout.
    """

    def __init__(self, topic, producer):
        """
        takes in the topic and the producer to send the messages through kafka
        :param topic: topic via which to send in the data
        :param producer: the instance of producer to encode the data and send through kafka.
        """
        super().__init__()
        self.topic = topic
        self.k_producer = producer

    def on_data(self, data) -> bool:
        """sends messages through kafka"""
        self.k_producer.send(self.topic, value=data)
        print(data)
        return True

    def on_error(self, status):
        """prints the status in case of errors"""
        print(status)


class TStreamer:
    """
    Class for streaming and processing live tweets.
    """

    def __init__(self, key, secret, token, token_secret):
        """
        requires twitter credentials to create streamer.
        can be acquired from twitter developer app page
        """
        self.CONSUMER_KEY = key
        self.CONSUMER_SECRET = secret
        self.ACCESS_TOKEN = token
        self.ACCESS_TOKEN_SECRET = token_secret

    def stream_tweets(self, hash_tags: list, listener: Listener):
        """
        uses twitter credentials to create streamer based on hash tags to filter by
        :param hash_tags: list of keywords to filter streams by
        :param listener: takes in an instance of the class listener to further process the stream
        """
        # This handles Twitter authentication and the connection to Twitter Streaming API
        auth = OAuthHandler(self.CONSUMER_KEY, self.CONSUMER_SECRET)
        auth.set_access_token(self.ACCESS_TOKEN, self.ACCESS_TOKEN_SECRET)
        stream = Stream(auth, listener)

        # This line filter Twitter Streams to capture data by the keywords:
        stream.filter(track=hash_tags)


if __name__ == '__main__':
    c_key = os.environ['API_KEY']
    c_secret = os.environ['API_SECRET_KEY']
    a_token = os.environ['ACCESS_TOKEN']
    a_secret = os.environ['ACCESS_TOKEN_SECRET']

    hash_tag_list = ["thursday"]

    stream_topic = "topic_one"
    kafka_producer = KafkaProducer(bootstrap_servers=['localhost:9092'],
                                   value_serializer=lambda x: x.encode('utf-8'))

    stream_listener = Listener(stream_topic, kafka_producer)
    t_streamer = TStreamer(c_key, c_secret, a_token, a_secret)
    t_streamer.stream_tweets(hash_tag_list, stream_listener)
