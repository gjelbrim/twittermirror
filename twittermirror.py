from tweepy import TweepError
from users import Sender as sender

"""
    main module
"""

try:
    s = sender()
    s.stream()
except TweepError as e:
    print(e)
