#!/usr/bin/env python

import tweepy
import random

CONSUMER_KEY = 'Your consumer key here'
CONSUMER_SECRET = 'Your consumer secret key here'
ACCESS_KEY = 'Your access key here'
ACCESS_SECRET = 'Your access secret key here'
MAX_TWEET_LENGTH = 137
FILE_TO_USE = "your quotes file here e.g quotes.txt"

def randomLine(afile):
	lines = open(afile).readlines()
	return lines[random.randint(0, len(lines))]

def makeArray(astring):
	noOfTweets = (len(astring)/MAX_TWEET_LENGTH)+1
	theArray = []
	while noOfTweets > 0:
		if noOfTweets == 1:
			theArray.append(astring)
		else:
			theArray.append(astring[:astring[:MAX_TWEET_LENGTH].rindex(" ")]+'...')
			astring = astring[astring[:MAX_TWEET_LENGTH].rindex(" "):]
		noOfTweets -= 1
	return theArray

	
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)
quoteString = randomLine(FILE_TO_USE)
tweetArray = makeArray(quoteString)

for tweet in reversed(tweetArray):
	api.update_status(tweet)
