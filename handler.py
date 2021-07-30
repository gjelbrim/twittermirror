from users import Receiver as receiver

class Handler:

    def __init__(self):
        self.rec = receiver()

    def handle(self,tweet):
        if not (tweet.startswith("@") or tweet.startswith("RT")):
            self.rec.tweet(tweet)
            print("tweeted "+tweet)
