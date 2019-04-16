import json
#Import the necessary methods from tweepy library
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream

print("Testing")
tweets_data_path = 'twitter_data.txt.'

tweets_data = []
tweets_file = open(tweets_data_path, "r")
for line in tweets_file:
    tweet = json.loads(line)
    print("First line of data: \n")
    print("Tweet ID: ", tweet['id'])
    print("Tweet: ", tweet['text'])
    user = tweet['user']
    print("Name: ", user['name'])
    print("Screen Name: ", user['screen_name'])
