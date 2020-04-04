package com.dimanche.example

import com.dimanche.examples.KafkaTwitterProducerExample.sendToKafka
import twitter4j._
import twitter4j.conf.ConfigurationBuilder

object TwitterStream {

    val consumerKey = sys.env.getOrElse("API_KEY", "")
    val consumerSecret = sys.env.getOrElse("API_SECRET_KEY", "")
    val accessToken = sys.env.getOrElse("ACCESS_TOKEN", "")
    val accessTokenSecret = sys.env.getOrElse("ACCESS_TOKEN_SECRET", "")

    if (consumerKey.isEmpty || consumerSecret.isEmpty || accessToken.isEmpty || accessTokenSecret.isEmpty) {
      throw new Exception(" At least one of the keys is not available from the environment variables ")
    }

    val twitterConf = new ConfigurationBuilder()
      .setJSONStoreEnabled(true)
      .setOAuthConsumerKey(consumerKey)
      .setOAuthConsumerSecret(consumerSecret)
      .setOAuthAccessToken(accessToken)
      .setOAuthAccessTokenSecret(accessTokenSecret)
      .build()

    def getStream = new TwitterStreamFactory(twitterConf).getInstance()

    class OnTweetPosted(cb: Status => Unit) extends StatusListener {

      override def onStatus(status: Status): Unit = {
        cb(status)
      }

      override def onException(ex: Exception): Unit = throw ex

      // no-op for the following events
      override def onStallWarning(warning: StallWarning): Unit = {}

      override def onDeletionNotice(statusDeletionNotice: StatusDeletionNotice): Unit = {}

      override def onScrubGeo(userId: Long, upToStatusId: Long): Unit = {}

      override def onTrackLimitationNotice(numberOfLimitedStatuses: Int): Unit = {}

    }

    def main(args: Array[String]): Unit = {

      val filters = new FilterQuery().track("trump")

      val twitterStream = TwitterStream.getStream
      twitterStream.addListener(new OnTweetPosted(status => println(status.getText)))
      twitterStream.filter(filters)
    }

}
