import sys
import tweepy
from config import Config as config

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
