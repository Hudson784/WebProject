import json
import re #Import for regular expressions
import pandas as pd
import matplotlib.pyplot as plt #Import for displaying charts

#Import the necessary methods from tweepy library
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream

#Variables that contains the user credentials to access Twitter API 
access_token = "1117652982475239424-TqGEsktbN74s0OGG6IqKKkXUArnSCi"
access_token_secret = "Xtf4rLv3z0N6nHt7yJvYsYPOjZwEC45N3oqRhKo87XVdb"
consumer_key = "uWrEWX2bhsMtN8hnpd12HjMfl"
consumer_secret = "bdcvgAI6xRTYvoHJeNf1nkDsl9oDylOkJr1gqkwXEasY3qK1EF"

ACCESS_TOKEN = '1117652982475239424-TqGEsktbN74s0OGG6IqKKkXUArnSCi'
ACCESS_SECRET = 'Xtf4rLv3z0N6nHt7yJvYsYPOjZwEC45N3oqRhKo87XVdb'
CONSUMER_KEY = 'uWrEWX2bhsMtN8hnpd12HjMfl'
CONSUMER_SECRET = 'bdcvgAI6xRTYvoHJeNf1nkDsl9oDylOkJr1gqkwXEasY3qK1EF'

#This is a basic listener that just prints received tweets to stdout.
class StdOutListener(StreamListener):

    def on_data(self, data):
        print(data)
        return True

    def on_error(self, status):
        print(status)

#Retrieves what was sent to the twitter_data.txt file 

if __name__ == '__main__':

    #This handles Twitter authetification and the connection to Twitter Streaming API
    l = StdOutListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    stream = Stream(auth, l)

    #This line filter Twitter Streams to capture data by the keywords: 'python', 'javascript', 'ruby'
    stream.filter(track=['python', 'javascript', 'ruby'])
