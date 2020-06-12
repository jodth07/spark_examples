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

    def on_connect(self):
        """Called once connected to streaming server.

        This will be invoked once a successful response
        is received from the server. Allows the listener
        to perform some work prior to entering the read loop.
        """
        print("Tweeter Stream connected")
        return True

    def on_data(self, raw_data):
        """sends messages through kafka"""
        self.k_producer.send(self.topic, value=raw_data)
        print(raw_data)
        return True

    def on_error(self, status_code):
        """
        Called when a non-200 status code is returned
        prints the status in case of errors
        """
        print(status_code)
        return False

    def on_warning(self, notice):
        """Called when a disconnection warning message arrives"""
        warning = "\n" + " * " * 10 + "\n"
        print(warning)
        print(notice)
        print(warning)
        return True

    def __repr__(self):
        output = f"This is is the listener for topic {self.topic}"
        return output


class TStreamer:
    """
    Class for streaming and processing live tweets.
    """

    def __init__(self, key, secret, token, token_secret):
        """
        requires twitter credentials to create streamer.
        can be acquired from twitter developer app page
        """
        self.consumer_key = key
        self.consumer_secret = secret
        self.access_token = token
        self.access_token_secret = token_secret

    def stream_tweets(self, hash_tags: list, listener: Listener):
        """
        uses twitter credentials to create streamer based on hash tags to filter by
        :param hash_tags: list of keywords to filter streams by
        :param listener: takes in an instance of the class listener to further process the stream
        """
        # This handles Twitter authentication and the connection to Twitter Streaming API
        auth = OAuthHandler(self.consumer_key, self.consumer_secret)
        auth.set_access_token(self.access_token, self.access_token_secret)
        stream = Stream(auth, listener)

        # This line filter Twitter Streams to capture data by the keywords:
        stream.filter(track=hash_tags)


if __name__ == '__main__':
    CONSUMER_KEY = os.environ['API_KEY']
    CONSUMER_SECRET = os.environ['API_SECRET_KEY']
    ACCESS_TOKEN = os.environ['ACCESS_TOKEN']
    ACCESS_TOKEN_SECRET = os.environ['ACCESS_TOKEN_SECRET']

    HASH_TAG_LIST = ["thursday"]

    STREAM_TOPIC = "topic_one"
    BOOTSTRAP_SERVERS = ['localhost:9092']

    kafka_producer = KafkaProducer(bootstrap_servers=BOOTSTRAP_SERVERS,
                                   value_serializer=lambda x: x.encode('utf-8'))

    stream_listener = Listener(STREAM_TOPIC, kafka_producer)
    t_streamer = TStreamer(CONSUMER_KEY, CONSUMER_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
    t_streamer.stream_tweets(HASH_TAG_LIST, stream_listener)
