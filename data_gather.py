#!/usr/bin/env python

import time
import sys
import json
import tweepy
import urllib3
from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener


def main():

  """
  Descripcion: usado solo para recolectar datos que se han mostrado en la presentacion del proyecto,
    recolectar todos los tweets con el hashtag '#heatMAD' y que tengan una localizacion y meterlos 
    en un archivo csv.
  """

  # Bot authentication.
  CONSUMER_KEY = ''
  CONSUMER_SECRET = ''
  ACCESS_KEY = ''
  ACCESS_SECRET = ''

  auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
  auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)

  api = tweepy.API(auth_handler=auth)

  hashtags = api.search(q="heatMAD")

  with open('coord.csv', 'a') as f:
    for status in hashtags:
      if status.coordinates:
        f.write(str(status.coordinates).split(':')[2][2:-2]+', '+status.user.name.encode('utf8')+', "'+status.text.encode('utf8')+'"\n')
  
if __name__ == '__main__':

  try:
    main()
  except KeyboardInterrupt:
    quit()
