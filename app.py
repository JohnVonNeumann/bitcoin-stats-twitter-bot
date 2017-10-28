import os
import re

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


def append_mempool_tx_count():
    """Return the mempool tx count"""
    getmempoolinfo = CLIENT.call('getmempoolinfo')
    fmt_getmempoolinfo = str(getmempoolinfo['size']) + ' tx in mempool'
    TWEET_LIST.append(fmt_getmempoolinfo)


def append_segwit_block_size():
    """Return the segwit tx data of the last block"""
    getbestblockhash = CLIENT.call('getbestblockhash')
    getblock = CLIENT.call('getblock', getbestblockhash)
    
    getblocksize = getblock['size']
    getstrippedsize = getblock['strippedsize']
    getsegwitsize = getblocksize / getstrippedsize
    
    segwitsize = '{:.1%}'.format(getsegwitsize - 1)
   
    strippedsize = str(getstrippedsize / 1000)
    slice_strippedsize = strippedsize[:4]

    for index, elem in enumerate(list(slice_strippedsize)):
        if index == 3 and elem == ".":
            re_strippedsize = slice_strippedsize[:3]
        else:
            re_strippedsize = slice_strippedsize

    blocksize = str(getblocksize / 1000)
    slice_blocksize = blocksize[:4]
    
    for index, elem in enumerate(list(slice_blocksize)):
        if index == 3 and elem == ".":
            re_blocksize = slice_blocksize[:3]
        else:
            re_blocksize = slice_blocksize

    
    fmt_blocksize = str("Last block " + re_blocksize + "kb")
    fmt_strippedsize = str("tx data in block: " + re_strippedsize +"kb")
    fmt_segwitsize = str("SegWit-Blocksize Ratio: " + segwitsize)
    TWEET_LIST.append(fmt_blocksize)
    TWEET_LIST.append(fmt_strippedsize)
    TWEET_LIST.append(fmt_segwitsize)

def format_list_and_post_tweet():
    """Creates string from TWEET_LIST append operations"""
    append_block_height()
    append_tx_per_second()
    append_mempool_tx_count()
    append_segwit_block_size()
    tweet = ' | '.join(TWEET_LIST)
    twitter = tweepy.API(TWITTER_AUTH)
    twitter.update_status(tweet)


if __name__ == "__main__":
    format_list_and_post_tweet()
