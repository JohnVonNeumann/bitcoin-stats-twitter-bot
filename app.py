import os

import tweepy
import bitcoin.rpc


CONSUMER_KEY = os.getenv('CONSUMER_KEY')
CONSUMER_SECRET = os.getenv('CONSUMER_SECRET')
ACCESS_TOKEN = os.getenv('ACCESS_TOKEN')
ACCESS_TOKEN_SECRET = os.getenv('ACCESS_TOKEN_SECRET')

CLIENT = bitcoin.rpc.Proxy()

TWITTER_AUTH = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
TWITTER_AUTH.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

TWEET_LIST = []


def block_number():
    """Return the current block height"""
    blocks = CLIENT.call('getblockcount')
    blocks_fmt = ('#' + str(blocks))
    TWEET_LIST.append(blocks_fmt)


def finished_tweet():
    """Creates string from TWEET_LIST append operations

    Returns:
        string: passed to update_status as user facing/formatted output
    """
    block_number()
    tweet = ''.join(TWEET_LIST)
    print(tweet)
    twitter = tweepy.API(TWITTER_AUTH)
    twitter.update_status(tweet)

finished_tweet()
