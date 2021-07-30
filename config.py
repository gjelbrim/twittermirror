from configparser import ConfigParser

"""
this module will configure twittermirror
"""

class Config:
    """
    class which holds the configuration setting
    """

    configuration = ConfigParser()
    configuration.read('config.ini')

    #keys of the sender account
    SENDER_API_KEY = configuration['sender']['APIKey']
    SENDER_API_SECRET_KEY = configuration['sender']['APISecretKey']
    SENDER_ACCESS_TOKEN = configuration['sender']['AccessToken']
    SENDER_ACCESS_TOKEN_SECRET = configuration['sender']['AccessTokenSecret']

    #keys of the receiver account
    RECEIVER_API_KEY = configuration['receiver']['APIKey']
    RECEIVER_API_SECRET_KEY = configuration['receiver']['APISecretKey']
    RECEIVER_ACCESS_TOKEN = configuration['receiver']['AccessToken']
    RECEIVER_ACCESS_TOKEN_SECRET = configuration['receiver']['AccessTokenSecret']

    #user to be mirrored
    TWITTER_USER = configuration['user']['TwitterHandle']
