#!/usr/bin/env python
# -*- coding: utf-8 -*-

import tweepy, time, sys, json, urllib, random, config, wget, os

auth = tweepy.OAuthHandler(config.TWITTER_CONSUMER_KEY, config.TWITTER_CONSUMER_SECRET)
auth.set_access_token(config.TWITTER_ACCESS_KEY, config.TWITTER_ACCESS_SECRET)
api = tweepy.API(auth)

//check YUDLbot, YUDLcat or YUDLdog for a retweetable tweet.

//check last rt, make sure not to duplicate.

//like Retweets of our stuff. Like items and then retweet from others.



for status in api.user_timeline(id="jpeak5",count=1):
  #api.create_favorite(status.id)
  #api.retweet(status.id)
  api.send_direct_message(user="jpeak5",text="we can only DM our followers. so I DM you.") #cannot dm those who don't follow
  


#for status in api.user_timeline(id="YUDLbot",count=1):
#  api.retweet(status.id)

#for item in tweepy.Cursor(api.user_timeline).items(1): #items() #pages() #page()
#  print(item)
