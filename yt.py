import httplib
import httplib2
import os
import random
import sys
import time

from apiclient.discovery import build
from apiclient.errors import HttpError
from oauth2client.client import Credentials

def get_yt_channel(youtube_id):
    print "get_yt_data"
    YOUTUBE_DATA_API_NAME = "youtube"
    YOUTUBE_DATA_API_VERSION = "v3"

    content = os.environ['YT']
    credentials = Credentials.new_from_json(content)
    http = httplib2.Http()
    http = credentials.authorize(http)
    youtube = build(YOUTUBE_DATA_API_NAME, YOUTUBE_DATA_API_VERSION, http=http)
    return youtube.channels().list(part='snippet', id=youtube_id).execute()
    