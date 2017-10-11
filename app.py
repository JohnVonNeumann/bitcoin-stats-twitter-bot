import os

import tweepy
import bitcoin.rpc

CONSUMER_KEY = os.getenv('CONSUMER_KEY')
CONSUMER_SECRET = os.getenv('CONSUMER_SECRET')
ACCESS_TOKEN = os.getenv('ACCESS_TOKEN')
ACCESS_TOKEN_SECRET = os.getenv('ACCESS_TOKEN_SECRET')

#client = bitcoin.rpc.Proxy()

twitter_auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
total_twitter_auth = twitter_auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

twitter = tweepy.API(total_twitter_auth)
twitter.update_status('test run')
