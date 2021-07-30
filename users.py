"""
module with the users
"""
import sys
import tweepy
from tweepy.error import TweepError
from config import Config as config

class Sender:
    """
    Sender sends the tweets to the receiver
    """

    def __init__(self):
        """
        inits the sender
        """
        try:
            oauth = tweepy.OAuthHandler(config.SENDER_API_KEY,config.SENDER_API_SECRET_KEY)
            oauth.set_access_token(config.SENDER_ACCESS_TOKEN,config.SENDER_ACCESS_TOKEN_SECRET)
        except TweepError:
            print ("Sender couldn't get authenticated")
            sys.exit()
        self.api = tweepy.API(oauth,wait_on_rate_limit=True)

    def stream(self):
        """
        will pass raw tweet to handler
        """
        rec = Receiver()
        last_tweet = ''
        while True:
            timeline = self.api.user_timeline
            tweet = tweepy.Cursor(timeline, screen_name=config.TWITTER_USER, tweet_mode="extended")
            for status in tweet.items(1):
                if status.full_text != last_tweet:
                    rec.tweet(status.full_text)
                    last_tweet = status.full_text

class Receiver:
    """
    will recive tweets from sender and tweet them
    """
    def __init__(self):
        """
        init of receiver
        """
        try:
            oauth = tweepy.OAuthHandler(config.RECEIVER_API_KEY,config.RECEIVER_API_SECRET_KEY)
            oauth.set_access_token(config.RECEIVER_ACCESS_TOKEN,config.RECEIVER_ACCESS_TOKEN_SECRET)
        except TweepError:
            print ("Receiver couldn't get authenticated")
            sys.exit()
        self.api = tweepy.API(oauth,wait_on_rate_limit=True)

    def tweet(self, tweet):
        """will send the tweet to Twitter

        Args:
            tweet ([str]): [tweet to be tweeted]
        """
        if not (tweet.startswith("@") or tweet.startswith("RT")):
            print("tweeted "+tweet)
        self.api.update_status(tweet)
