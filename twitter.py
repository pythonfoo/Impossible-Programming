import tweepy
from twitter_keys import get_keys

keys = get_keys()

consumer_key = keys["consumer_key"]
consumer_secret = keys["consumer_secret"]
access_token = keys["access_token"]
access_token_secret = keys["access_token_secret"]

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

max_len = 140 - 6

def tweet(text):
    api.update_status(text)

def tweet_job(job):
    if len(job) <= max_len:
        job = "[Bot] " + job
        tweet(job)
    else:
        print("Tut mir leid, das Zeichenlimit wurde erreicht")