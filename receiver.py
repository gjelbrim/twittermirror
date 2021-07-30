from config import Config as config
import tweepy

class Receiver:
    def OAuth(self):
        try:
            auth = tweepy.OAuthHandler(config.RECEIVER_API_KEY,config.RECEIVER_API_SECRET_KEY)
            auth.set_access_token(config.RECEIVER_ACCESS_TOKEN,config.RECEIVER_ACCESS_TOKEN_SECRET)
            return auth
        except Exception as e:
            print ("Receiver couldn't get authenticated")
            exit(1)
            
    def __init__(self):
        oauth = self.OAuth()
        self.api = tweepy.API(oauth,wait_on_rate_limit=True)

    def tweet(self, tweet):
        self.api.update_status(tweet)