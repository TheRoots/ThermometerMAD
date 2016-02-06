#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time
import sys
import json
import tweepy
import urllib3
from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener


class listener(StreamListener):

  def on_status(self, status):
    if status.coordinates:
      with open('coords.csv', 'a') as f:
        f.write(str(status.coordinates).split(':')[2][2:-2]+'\n')
    return True

  on_event = on_status

  def on_error(self, status):
    print status

def main():

  # Bot authentication.
  CONSUMER_KEY = ''
  CONSUMER_SECRET = ''
  ACCESS_KEY = ''
  ACCESS_SECRET = ''

  auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
  auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)

  api = tweepy.API(auth_handler=auth)
	
  print ''
  twitterStream = Stream(auth, listener())
  twitterStream.filter(track=['a'])

if __name__ == '__main__':

  try:
    main()
  except KeyboardInterrupt:
    quit()


