from tweepy import TweepError
from sender import Sender as sender

try:
    s = sender()
    s.stream()
except TweepError as e:
    print(e)