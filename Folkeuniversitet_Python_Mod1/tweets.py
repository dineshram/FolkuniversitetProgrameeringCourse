__author__ = 'dram'

from urllib.request import urlopen
import json

screen_name = "@POTUS"

url = "http://api.twitter.com/1/statuses/user_timeline.json?screen_name=" + screen_name

data = json.load(urlopen(url))

print(len(data), "tweets")

for tweet in data:
    print(tweet['text'])
