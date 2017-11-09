#!/usr/bin/env python
# -*- coding: utf-8 -*-

import tweepy, time, sys, json, urllib, random, config

auth = tweepy.OAuthHandler(config.TWITTER_CONSUMER_KEY, config.TWITTER_CONSUMER_SECRET)
auth.set_access_token(config.TWITTER_ACCESS_KEY, config.TWITTER_ACCESS_SECRET)
api = tweepy.API(auth)

response = urllib.urlopen(config.SOLR_DATA);
data = json.loads(response.read())
docs = data["response"]["docs"]

items = random.sample(docs,1)

response = urllib.urlopen(solr_data);
data = json.loads(response.read())
docs = data["response"]["docs"]

items = random.sample(docs,1)

for item in items:
  pid = item["PID"]
  description = item["mods_abstract_s"][0]
  if len(description) > 257:
    while len(description) + 3 > 256:
        description = description[:len(description) - 1]
    description = description + '...'
  title = item["mods_titleInfo_title_s"][0]
  if len(title) > 257:
    while len(title) + 3 > 256:
        title = title[:len(title) - 1]
    title = title + '...'
  url = "http://digital.library.yorku.ca/islandora/object/"
  url += pid
  tweet_text = "%s %s" % (description,url)
  api.update_status(tweet_text)

