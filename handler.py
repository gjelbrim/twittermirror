from users import Receiver as receiver

"""
this module handles tweet updates
"""

class Handler:
    """
    class to handle tweet updates
    """
    def __init__(self):
        """will init the receiver
        """
        self.rec = receiver()

    def handle(self,tweet):
        """will tweet the tweet

        Args:
            tweet ([str]): [the raw tweet that will be handled]
        """
        if not (tweet.startswith("@") or tweet.startswith("RT")):
            self.rec.tweet(tweet)
            print("tweeted "+tweet)
