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


def append_block_height():
    """Return the current block height"""
    getblockcount = CLIENT.call('getblockcount')
    fmt_getblockcount = ('#' + str(getblockcount))
    TWEET_LIST.append(fmt_getblockcount)


def append_tx_per_second():
    """Return the current tx per second"""
    getchaintxstats = CLIENT.call('getchaintxstats')
    txrate = str(getchaintxstats['txrate'])
    fmt_txrate = txrate[:4] + 'txps'
    TWEET_LIST.append(fmt_txrate)


def format_list_and_post_tweet():
    """Creates string from TWEET_LIST append operations

    Returns:
        string: passed to update_status as user facing/formatted output
    """
    append_block_height()
    append_tx_per_second()
    tweet = ' '.join(TWEET_LIST)
    twitter = tweepy.API(TWITTER_AUTH)
    twitter.update_status(tweet)


format_list_and_post_tweet()
