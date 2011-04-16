#!/usr/bin/env python

import tweepy
import random

CONSUMER_KEY = 'Your consumer key here'
CONSUMER_SECRET = 'Your consumer secret key here'
ACCESS_KEY = 'Your access key here'
ACCESS_SECRET = 'Your access secret key here'
MAX_TWEET_LENGTH = 140
FILE_TO_USE = "your quotes file here e.g quotes.txt"

def randomLine(afile):
	lines = open(afile).readlines()
	return lines[random.randint(0, len(lines)-1)]

def makeArray(astring):
	try:
		astring.index("\n")
		astring = sanatiseString(astring)
	except ValueError:
		#No return character found, string is fine as is.
	
	if len(astring)%MAX_TWEET_LENGTH == 0:
		noOfTweets = len(astring)/MAX_TWEET_LENGTH
	else:
		noOfTweets = (len(astring)/MAX_TWEET_LENGTH)+1

	theArray = []
	while noOfTweets > 0:
		if noOfTweets == 1:
			theArray.append(astring)
		else:
			theArray.append(astring[:astring[:MAX_TWEET_LENGTH-2].rindex(" ")]+'...')
			astring = astring[astring[:MAX_TWEET_LENGTH-2].rindex(" "):]
		noOfTweets -= 1
	return theArray

def sanatiseString(astring):
	sanatisedString = astring[:astring.index("\n")]
	return sanatisedString
	
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)
quoteString = randomLine(FILE_TO_USE)
tweetArray = makeArray(quoteString)

for tweet in reversed(tweetArray):
	api.update_status(tweet)
