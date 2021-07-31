"""
    main module
"""
import re
from tweepy import TweepError
import users

try:
    sender = users.Sender()
    receiver = users.Receiver()
except TweepError as e:
    print(e)

print("Users authenticated.")
own_last_tweet = receiver.get_own_last_tweet()
users_last_tweet = sender.get_users_last_tweet()
print("your last tweet was: "+own_last_tweet)
print("their last tweet was: "+ users_last_tweet)

while True:
    own_last_tweet = receiver.get_own_last_tweet()
    users_last_tweet = sender.get_users_last_tweet()
    #@ will be changed to (@) to avoid involving other users
    tweet = users_last_tweet.replace("@","(@)")
    #urls change on mirroring so they will be deleted for comparison
    comparison_own_tweet = re.sub(r"http\S+", "", own_last_tweet)
    comparison_users_tweet = re.sub(r"http\S+", "", users_last_tweet.replace("@","(@)"))

    if comparison_users_tweet != comparison_own_tweet:
        receiver.tweet(tweet)
