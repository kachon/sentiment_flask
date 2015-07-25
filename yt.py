import httplib
import httplib2
import os
import random
import sys
import time

from apiclient.discovery import build
from apiclient.errors import HttpError
from oauth2client.client import Credentials
from sentiment import SentimentClf

class Yt(object):

  def __init__(self):
    YOUTUBE_DATA_API_NAME = "youtube"
    YOUTUBE_DATA_API_VERSION = "v3"
    content = os.environ['YT']
    credentials = Credentials.new_from_json(content)
    http = httplib2.Http()
    http = credentials.authorize(http)
    self.youtube = build(YOUTUBE_DATA_API_NAME, YOUTUBE_DATA_API_VERSION, http=http)

  def get_channel(self, channel_id):
    print "get_yt_data"
    return self.youtube.channels().list(part='snippet', id=youtube_id).execute()

  def get_videos(self, channel_id):
    print "get_yt_videos"
    #self.youtube.search().list(part='snippet', channelId='UC3vDyPXJ2AB_P5sTbgeaf1g', order='date', type='video').execute()
    results = self.youtube.search().list(part="snippet", channelId=channel_id, order="date", type="video").execute()
    vids = []
    for item in results["items"]:
      vid = item["id"]["videoId"]
      vids.append(vid)
    return vids

  def get_video_comment(self, video_id):
    results = self.youtube.commentThreads().list(part="snippet", order='time', videoId=video_id).execute()
    comments = []
    for item in results["items"]:
      comments.append(item["snippet"]["topLevelComment"]["snippet"]["textDisplay"]) 
    return " ".join(comments)

  def get_videos_comment(self, video_ids):
    comments = []
    #for vid in video_ids:
    for vid in video_ids:
      comments.append({"vid" : vid, "comment" : self.get_video_comment(vid)})
    return comments

  def get_channel_comments(self, channel_id):
    vids = self.get_videos(channel_id)
    comments = self.get_videos_comment(vids)
    return comments




