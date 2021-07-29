from sender import Sender as sender
from tweepy import TweepError

try:
    s = sender() 
    s.stream()
except TweepError as e:
    print(e)