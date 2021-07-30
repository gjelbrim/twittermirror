from config import Config as config
import tweepy
#import time
from handler import Handler as handler

class Sender:
    def o_auth(self):
        try:
            auth = tweepy.OAuthHandler(config.SENDER_API_KEY,config.SENDER_API_SECRET_KEY)
            auth.set_access_token(config.SENDER_ACCESS_TOKEN,config.SENDER_ACCESS_TOKEN_SECRET)
            return auth
        except Exception as e:
            print ("Sender couldn't get authenticated")
            exit(1)
            
    def __init__(self):
        oauth = self.o_auth()
        self.api = tweepy.API(oauth,wait_on_rate_limit=True)
        
    def stream(self):
        last_tweet = ''
        tweet_handler = handler()
        while True:
            for status in tweepy.Cursor(self.api.user_timeline, screen_name=config.TWITTER_USER, tweet_mode="extended").items(1):
                if status.full_text != last_tweet:
                    tweet_handler.handle(status.full_text)
                    last_tweet = status.full_text
                    #time.sleep(120)