"""
module with the users
"""
import sys
import tweepy
from tweepy.error import TweepError
from config import Config as conf

class Sender:
    """
    Sender sends the tweets to the receiver
    """

    def __init__(self):
        """
        inits the sender
        """
        try:
            oauth = tweepy.OAuthHandler(conf.SENDER_API_KEY,conf.SENDER_API_SECRET_KEY)
            oauth.set_access_token(conf.SENDER_ACCESS_TOKEN,conf.SENDER_ACCESS_TOKEN_SECRET)
        except TweepError:
            print ("Sender couldn't get authenticated")
            sys.exit()
        self.api = tweepy.API(oauth,wait_on_rate_limit=True)

    def get_users_last_tweet(self):
        """
        will return the last tweet of the user to be mirrored
        Returns:
            str: last tweet of the user to be mirrored
        """
        tweet = ""
        for status in tweepy.Cursor(self.api.user_timeline, screen_name=conf.TWITTER_USER).items(1):
            tweet = status.text
        return tweet


class Receiver:
    """
    will receive tweets from sender and tweet them
    """
    def __init__(self):
        """
        init of receiver
        """
        try:
            oauth = tweepy.OAuthHandler(conf.RECEIVER_API_KEY,conf.RECEIVER_API_SECRET_KEY)
            oauth.set_access_token(conf.RECEIVER_ACCESS_TOKEN,conf.RECEIVER_ACCESS_TOKEN_SECRET)
        except TweepError:
            print ("Receiver couldn't get authenticated")
            sys.exit()
        self.api = tweepy.API(oauth,wait_on_rate_limit=True)

    def tweet(self, tweet):
        """will send the tweet to Twitter

        Args:
            tweet str: tweet to be tweeted
        """
        self.api.update_status(tweet)

    def get_own_last_tweet(self):
        """
        returns own last tweets

        Returns:
            str: last own tweet
        """
        last_tweet = ''
        for status in tweepy.Cursor(self.api.user_timeline).items(1):
            last_tweet = status.text
        return last_tweet
