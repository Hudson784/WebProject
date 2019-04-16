import json
import pandas as pd
import matplotlib.pyplot as plt

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

tweets_data_path = 'twitter_data.txt.'

tweets_data = []
tweets_file = open(tweets_data_path, "r")
for line in tweets_file:
    try:
        tweet = json.loads(line)
        tweets_data.append(tweet)
    except:
        continue

print(len(tweets_data))
tweets = pd.DataFrame()
tweets['text'] = map(lambda tweet: tweet['text'], tweets_data)
tweets['lang'] = map(lambda tweet: tweet['lang'], tweets_data)
tweets['country'] = map(lambda tweet: tweet['place']['country'] if tweet['place'] != None else None, tweets_data)

tweets_by_lang = tweets['lang'].value_counts()

fig, ax = plt.subplots()
ax.tick_params(axis='x', labelsize=15)
ax.tick_params(axis='y', labelsize=10)
ax.set_xlabel('Languages', fontsize=15)
ax.set_ylabel('Number of tweets' , fontsize=15)
ax.set_title('Top 5 languages', fontsize=15, fontweight='bold')
tweets_by_lang[:5].plot(ax=ax, kind='bar', color='red')

if __name__ == '__main__':

    #This handles Twitter authetification and the connection to Twitter Streaming API
    l = StdOutListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    stream = Stream(auth, l)

    #This line filter Twitter Streams to capture data by the keywords: 'python', 'javascript', 'ruby'
    stream.filter(track=['python', 'javascript', 'ruby'])