#!/usr/bin/env python
# -*- coding: utf-8 -*-

import tweepy, time, sys, json, urllib, random, bitly_api, config

auth = tweepy.OAuthHandler(config.TWITTER_CONSUMER_KEY, config.TWITTER_CONSUMER_SECRET)
auth.set_access_token(config.TWITTER_ACCESS_KEY, config.TWITTER_ACCESS_SECRET)
api = tweepy.API(auth)

b = bitly_api.Connection(config.BITLY_API_USER, config.BITLY_API_KEY)

response = urllib.urlopen(config.SOLR_DATA);
data = json.loads(response.read())
docs = data["response"]["docs"]

items = random.sample(docs,1)

for item in items:
  pid = item["PID"]
  title = item["mods_titleInfo_title_ms"][0]
  url = "http://digital.library.yorku.ca/islandora/object/"
  url += pid
  shorten_url = b.shorten(url)
  bitly_url = shorten_url["url"]
  tweet_text = "%s %s" % (title,bitly_url)
  api.update_status(tweet_text)
