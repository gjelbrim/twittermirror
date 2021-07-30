"""
    installation process
"""
from configparser import ConfigParser
import subprocess
import sys

subprocess.call([sys.executable, "-m","pip3", "install", "-r", "requirements.txt" ])

print("requirements installed successfully.")
print("--------------------------------")
print("Keys of the account which will READ the tweets")
senderAPIKey = input("Enter API Key: ")
senderAPISecretKey = input("Enter API Secret Key: ")
senderAccessToken = input("Enter access token: ")
senderAccessTokenSecret = input("Enter access token secret: ")
print("--------------------------------")
print("Keys of the account which will tweet the tweets")
receiverAPIKey = input("Enter API Key: ")
receiverAPISecretKey = input("Enter API Secret Key: ")
receiverAccessToken = input("Enter access token: ")
receiverAccessTokenSecret = input("Enter access token secret: ")
print("--------------------------------")
twitterUser = input("Enter Twitter handle of user to be mirrored: ")
print()
print("--------------------------------")


def check_handle():
    """checks if the handle is in the right format, fix it if not

    Returns:
        [string]: [the handle in the right format]
    """
    if twitterUser.startswith("@"):
        return twitterUser
    return "@"+twitterUser

config = ConfigParser()

config['sender'] = {
    'APIKey': senderAPIKey,
    'APISecretKey': senderAPISecretKey,
    'AccessToken': senderAccessToken,
    'AccessTokenSecret': senderAccessTokenSecret
}

config['receiver'] = {
    'APIKey': receiverAPIKey,
    'APISecretKey': receiverAPISecretKey,
    'AccessToken': receiverAccessToken,
    'AccessTokenSecret': receiverAccessTokenSecret
}

config['user'] = {
    'TwitterHandle': check_handle()
    }

with open("config.ini", "w") as file:
    config.write(file)

print("installation complete")
