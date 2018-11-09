import tweepy
from textblob import TextBlob

consumer_key = 'KjfDPAuTEXXEezG5O9l9hLZtv'
consumer_secret = 'bnjJ8vzsXTKlhybRsidBs0UuuG5KSyK0GWFn4XfVdq3rkN6aws'

access_token = '121784450-L9619ywBIAcS7Om6bMoZrUWRPgfphAjRABtgs854'
access_token_secret = 'inwd3nM4orFxyxa20ExgjU8mMgqXsFmgQL8K39ZEkqKRo'

auth = tweepy.OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_token,access_token_secret)

api = tweepy.API(auth)

public_tweets = api.search('MachineLearning')

for tweet in public_tweets:
    print(tweet.text)
    analysis = TextBlob(tweet.text)
    print(analysis.sentiment)
