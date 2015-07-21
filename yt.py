import httplib
import httplib2
import os
import random
import sys
import time

from apiclient.discovery import build
from apiclient.errors import HttpError
from oauth2client.client import Credentials

class Yt(object):

  def __init__(self):
    YOUTUBE_DATA_API_NAME = "youtube"
    YOUTUBE_DATA_API_VERSION = "v3"
    content = os.environ['YT']
    credentials = Credentials.new_from_json(content)
    http = httplib2.Http()
    http = credentials.authorize(http)
    self.youtube = build(YOUTUBE_DATA_API_NAME, YOUTUBE_DATA_API_VERSION, http=http)

  def get_yt_channel(self, youtube_id):
    print "get_yt_data"
    return self.youtube.channels().list(part='snippet', id=youtube_id).execute()

  def get_yt_videos(self, youtube_id):
    print "get_yt_videos"
    #self.youtube.search().list(part='snippet', channelId='UC3vDyPXJ2AB_P5sTbgeaf1g', order='date', type='video').execute()
    return self.youtube.search
