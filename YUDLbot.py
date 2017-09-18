#!/usr/bin/env python
# -*- coding: utf-8 -*-

import tweepy, time, sys, json, urllib, random, config, wget, os

auth = tweepy.OAuthHandler(config.TWITTER_CONSUMER_KEY, config.TWITTER_CONSUMER_SECRET)
auth.set_access_token(config.TWITTER_ACCESS_KEY, config.TWITTER_ACCESS_SECRET)
api = tweepy.API(auth)
response = urllib.request.urlopen(config.SOLR_DATA);
data = response.read()
decoded = data.decode('utf-8')
d_json = json.loads(decoded)
docs = d_json["response"]["docs"]
items = random.sample(docs,1)

# test_tweet='this is a test, of a new P.Pelican_YUDLbot'
# api.update_status(test_tweet)

for item in items:
  pid = item["PID"]
  description = item["mods_abstract_mt"][0]
 
  if len(description) > 51:
    print()
    while len(description) + 3 > 50:
        description = description[:len(description) - 1]
    description = description + '...'
  title = item["mods_titleInfo_title_ms"][0]
  if len(title) > 51:
    while len(title) + 3 > 50:
        title = title[:len(title) - 1]
    title = title
  url = "http://test.louisianadigitallibrary.org/islandora/object/"
  url += pid
  TN = url + '/datastream/TN/view.jpeg'
  image = wget.download(TN)
  #write(image, 'view.jpeg')
  tweet_text = "%s %s" % (description,url)
  print(tweet_text)
  api.update_with_media('view.jpeg',status=tweet_text)
  os.remove('view.jpeg')