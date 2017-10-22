import os
import codecs

import tweepy
import bitcoin.rpc

consumer_key = os.getenv('CONSUMER_KEY')
consumer_secret = os.getenv('CONSUMER_SECRET')
access_token = os.getenv('ACCESS_TOKEN')
access_token_secret = os.getenv('ACCESS_TOKEN_SECRET')

twitter_auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
twitter_auth.set_access_token(access_token, access_token_secret)

twitter = tweepy.API(twitter_auth)
twitter.update_status('And another one.')
