from receiver import Receiver as receiver

class Handler:
    
    def __init__(self):
        self.r = receiver()
        
    def handle(self,tweet):
        if not (tweet.startswith("@") or tweet.startswith("RT")):
            self.r.tweet(tweet)
            print("tweeted "+tweet)