package com.dimanche.examples;

import twitter4j.*;
import twitter4j.conf.ConfigurationBuilder;

import java.util.Map;
import java.util.concurrent.LinkedBlockingQueue;

public class TwitterStreamer {

    public static TwitterStream getStreamer() {

        Map<String, String> env = System.getenv();
        String consumerKey = env.get("API_KEY");
        String consumerSecret = env.get("API_SECRET_KEY");
        String accessToken = env.get("ACCESS_TOKEN");
        String accessTokenSecret = env.get("ACCESS_TOKEN_SECRET");

        ConfigurationBuilder cb = new ConfigurationBuilder();
        cb.setDebugEnabled(true)
                .setOAuthConsumerKey(consumerKey)
                .setOAuthConsumerSecret(consumerSecret)
                .setOAuthAccessToken(accessToken)
                .setOAuthAccessTokenSecret(accessTokenSecret)
                .setJSONStoreEnabled(true);

        return new TwitterStreamFactory(cb.build()).getInstance();
    }


    public static StatusListener getListener(final LinkedBlockingQueue<String> queue){

        return new StatusListener() {

            public void onStatus(Status status) {
                String tweets = TwitterObjectFactory.getRawJSON(status);
                queue.offer(tweets);
            }

            public void onDeletionNotice(StatusDeletionNotice statusDeletionNotice) {
                System.out.println("Got a status deletion notice id:"
                        + statusDeletionNotice.getStatusId());
            }

            public void onTrackLimitationNotice(int numberOfLimitedStatuses) {
                System.out.println("Got track limitation notice:" +
                        numberOfLimitedStatuses);
            }

            public void onScrubGeo(long userId, long upToStatusId) {
                System.out.println("Got scrub_geo event userId:" + userId +
                        "upToStatusId:" + upToStatusId);
            }

            public void onStallWarning(StallWarning warning) {
                System.out.println("Got stall warning:" + warning);
            }

            public void onException(Exception ex) {
                ex.printStackTrace();
            }
        };
    }


    /*
    public static void main(String[] args) throws Exception {

        final LinkedBlockingQueue<Status> queue = new LinkedBlockingQueue<Status>(1000);
        TwitterStream twitterStream = getStreamer();
        StatusListener listener = getListener(queue);
        twitterStream.addListener(listener);

        String[] keyWords = {"nentindo", "switch", "switches"};
        FilterQuery query = new FilterQuery().track(keyWords);
        twitterStream.filter(query);

        Thread.sleep(5000);


        int i = 0;

        while (i < 10) {
            Status ret = queue.poll();

            if (ret == null) {
                Thread.sleep(100);
                i++;
            } else {

                Status tweet = queue.take();
                Long id = tweet.getId();

                System.out.println(tweet.toString()
                );
            }
        }

        Thread.sleep(5000);
        twitterStream.shutdown();
    }
    */
}