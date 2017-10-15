import os

import tweepy
import bitcoin.rpc

CONSUMER_KEY = os.getenv('CONSUMER_KEY')
CONSUMER_SECRET = os.getenv('CONSUMER_SECRET')
ACCESS_TOKEN = os.getenv('ACCESS_TOKEN')
ACCESS_TOKEN_SECRET = os.getenv('ACCESS_TOKEN_SECRET')

client = bitcoin.rpc.Proxy()

blocks = client.call('getblockcount')
print('#' + str(blocks))

mempool = client.call('getmempoolinfo')
print(str(mempool['size']) + ' transactions awaiting confirmation')

fee = client.call('estimatesmartfee', 6)
print(fee)


#twitter_auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
#twitter_auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
#
#twitter = tweepy.API(twitter_auth)
#twitter.update_status('And I was given life.')
