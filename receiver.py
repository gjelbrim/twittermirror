import tweepy
from config import Config as config
import sys

class Receiver:
    def o_auth(self):
        try:
            auth = tweepy.OAuthHandler(config.RECEIVER_API_KEY,config.RECEIVER_API_SECRET_KEY)
            auth.set_access_token(config.RECEIVER_ACCESS_TOKEN,config.RECEIVER_ACCESS_TOKEN_SECRET)
            return auth
        except Exception:
            print ("Receiver couldn't get authenticated")
            sys.exit(1)

    def __init__(self):
        oauth = self.o_auth()
        self.api = tweepy.API(oauth,wait_on_rate_limit=True)

    def tweet(self, tweet):
        self.api.update_status(tweet)
