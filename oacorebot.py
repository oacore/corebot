import tweepy
import requests
import json
import urllib
# Import our Twitter credentials from parameters.py
from parameters import *

class OAcorebotStreamListener(tweepy.StreamListener):

    def on_status(self, status):
        url="http://core.ac.uk/api-v2/articles/search?apiKey="+core_api_key
        payload = {"query":status.text, "pageSize":1}
        print (payload)
        r = requests.post(url, params = payload)
        print(r.text)

# Access and authorize our Twitter credentials from credentials.py
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)
oacorebotStreamListener = OAcorebotStreamListener()
oacorebotStream = tweepy.Stream(auth = api.auth, listener=OAcorebotStreamListener())
oacorebotStream.filter(track=['#milan'])



