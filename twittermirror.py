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
print("your last tweet was: "+own_last_tweet.full_text)
print("their last tweet was: "+ users_last_tweet.full_text)

while True:
    own_last_tweet = receiver.get_own_last_tweet()
    users_last_tweet = sender.get_users_last_tweet()

    #urls change on mirroring so they will be deleted for comparison
    comparison_own_tweet = re.sub(r"http\S+", "", own_last_tweet.full_text)
    comparison_users_tweet = re.sub(r"http\S+", "", users_last_tweet.full_text.replace("@","(@)"))

    both_retweeted =\
    'retweeted_status' in dir(own_last_tweet) and 'retweeted_status' in dir(own_last_tweet)
    same_retweet = False
    if(both_retweeted):
        same_retweet = own_last_tweet.retweeted_status.id == users_last_tweet.retweeted_status.id

    if ((comparison_users_tweet != comparison_own_tweet) and not(both_retweeted and same_retweet)):
        receiver.tweet(users_last_tweet)
