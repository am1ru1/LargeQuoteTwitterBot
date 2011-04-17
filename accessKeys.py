import tweepy
import sys

CONSUMER_KEY = sys.argv[1]
CONSUMER_SECRET_KEY = sys.argv[2]

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET_KEY)
authURL = auth.get_authorization_url()
print 'Authorization url: ' + authURL
verifyPIN = raw_input('Verification PIN: ').strip()
auth.get_access_token(verifyPIN)
print "Your ACCESS_KEY = '%s'" % auth.access_token.key
print "Your ACCESS_SECRET = '%s'" % auth.access_token.secret
