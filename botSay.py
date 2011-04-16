#!/usr/bin/env python
 
import sys
import tweepy

CONSUMER_KEY = 'Your consumer key here'
CONSUMER_SECRET = 'Your consumer secret key here'
ACCESS_KEY = 'Your access key here'
ACCESS_SECRET = 'Your access secret key here'

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)
api.update_status(sys.argv[1])
