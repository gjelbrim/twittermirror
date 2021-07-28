from configparser import ConfigParser

class Config:

    config = ConfigParser()
    config.read('config.ini')
    
    #keys of the sender account
    SENDER_API_KEY = config['sender']['APIKey']
    SENDER_API_SECRET_KEY = config['sender']['APISecretKey']
    SENDER_ACCESS_TOKEN = config['sender']['AccessToken']
    SENDER_ACCESS_TOKEN_SECRET = config['sender']['AccessTokenSecret']

    #keys of the receiver account
    RECEIVER_API_KEY = config['receiver']['APIKey']
    RECEIVER_API_SECRET_KEY = config['receiver']['APISecretKey']
    RECEIVER_ACCESS_TOKEN = config['receiver']['AccessToken']
    RECEIVER_ACCESS_TOKEN_SECRET = config['receiver']['AccessTokenSecret']

    #user to be mirrored
    #TWITTER_USER = config['user']['TwitterHandle']
