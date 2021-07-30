import sys
import tweepy
from config import Config as config
from handler import Handler as handler

class Sender:

    def __init__(self):
        try:
            oauth = tweepy.OAuthHandler(config.SENDER_API_KEY,config.SENDER_API_SECRET_KEY)
            oauth.set_access_token(config.SENDER_ACCESS_TOKEN,config.SENDER_ACCESS_TOKEN_SECRET)
        except Exception:
                print ("Sender couldn't get authenticated")
                sys.exit()
        self.api = tweepy.API(oauth,wait_on_rate_limit=True)

    def stream(self):
        last_tweet = ''
        tweet_handler = handler()
        while True:
            timeline = self.api.user_timeline
            tweet = tweepy.Cursor(timeline, screen_name=config.TWITTER_USER, tweet_mode="extended")
            for status in tweet.items(1):
                if status.full_text != last_tweet:
                    tweet_handler.handle(status.full_text)
                    last_tweet = status.full_text

class Receiver:
    def __init__(self):
        try:
            oauth = tweepy.OAuthHandler(config.RECEIVER_API_KEY,config.RECEIVER_API_SECRET_KEY)
            oauth.set_access_token(config.RECEIVER_ACCESS_TOKEN,config.RECEIVER_ACCESS_TOKEN_SECRET)
        except Exception:
            print ("Receiver couldn't get authenticated")
            sys.exit(1)
        self.api = tweepy.API(oauth,wait_on_rate_limit=True)

    def tweet(self, tweet):
        self.api.update_status(tweet)
