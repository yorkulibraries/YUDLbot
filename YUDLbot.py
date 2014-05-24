#!/usr/bin/env python
# -*- coding: utf-8 -*-

import tweepy, time, sys, json, urllib, random, bitly_api

CONSUMER_KEY = 'something'
CONSUMER_SECRET = 'something'
ACCESS_KEY = 'something'
ACCESS_SECRET = 'something'
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)

BITLY_API_USER = "something"
BITLY_API_KEY = "something"

b = bitly_api.Connection(BITLY_API_USER, BITLY_API_KEY)

url = 'http://localhost/solr/yudl/select?q=YOURSOLRQUERY&wt=json&indent=true'

response = urllib.urlopen(url);
data = json.loads(response.read())
docs = data["response"]["docs"]

items = random.sample(docs,1)
#response.close()

for item in items:
  pid = item["PID"]
  title = item["mods_titleInfo_title_ms"][0]
  url = "http://digital.library.yorku.ca/islandora/object/"
  url += pid
  shorten_url = b.shorten(url)
  bitly_url = shorten_url["url"]
  tweet_text = z = "%s %s" % (title,bitly_url)
  api.update_status(tweet_text)
