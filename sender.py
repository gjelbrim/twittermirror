import tweepy
from config import Config as config
import sys
from handler import Handler as handler

class Sender:
    def o_auth(self):
        try:
            auth = tweepy.OAuthHandler(config.SENDER_API_KEY,config.SENDER_API_SECRET_KEY)
            auth.set_access_token(config.SENDER_ACCESS_TOKEN,config.SENDER_ACCESS_TOKEN_SECRET)
            return auth
        except Exception:
            print ("Sender couldn't get authenticated")
            sys.exit()

    def __init__(self):
        oauth = self.o_auth()
        self.api = tweepy.API(oauth,wait_on_rate_limit=True)

    def stream(self):
        last_tweet = ''
        tweet_handler = handler()
        while True:
            tweet = tweepy.Cursor(self.api.user_timeline, screen_name=config.TWITTER_USER, tweet_mode="extended").items(1)
            for status in tweet:
                if status.full_text != last_tweet:
                    tweet_handler.handle(status.full_text)
                    last_tweet = status.full_text
