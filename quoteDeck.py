#!/usr/bin/env python

import tweepy
import random

CONSUMER_KEY = 'Your consumer key here'
CONSUMER_SECRET = 'Your consumer secret key here'
ACCESS_KEY = 'Your access key here'
ACCESS_SECRET = 'Your access secret key here'
MAX_TWEET_LENGTH = 140
FILE_TO_USE = "quotesfile.txt"
tweetArray = []

def randomLine(afile):
	lines = open(afile).readlines()
	return lines[random.randint(0, (len(lines))-1)]

def makeArray(astring):
	try:
		astring.index("\n")
		astring = sanatiseString(astring)
	except ValueError:
		print "No return character found, string is fine as is."
	addToArray(astring)
	
def addToArray(astring):

	if len(astring) <= 140:
		tweetArray.append(astring)
	else:
		tweetArray.append(astring[:astring[:MAX_TWEET_LENGTH-3].rindex(' ')]+'...')
		addToArray(astring[astring[:MAX_TWEET_LENGTH-3].rindex(' ')+1:len(astring)])

def sanatiseString(astring):
	sanatisedString = astring[:astring.index("\n")]
	return sanatisedString
	
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)
quoteString = randomLine(FILE_TO_USE)
makeArray(quoteString)

for tweet in reversed(tweetArray):
	api.update_status(tweet)
