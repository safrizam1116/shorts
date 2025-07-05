import time, json, os
from datetime import datetime
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload
from oauth2client.tools import run_flow
from oauth2client.file import Storage

def jam_ganjil():
    now = datetime.now()
    return now.hour % 2 == 1 and now.minute == 0

def ambil_video_belum_upload():
    uploaded = json.load(open("logs/uploaded.json"))
    for f in sorted(os.listdir("output/")):
        if f not in uploaded:
            return f
    return None

def upload(video_path):
    # YouTube API upload logic di sini
    pass

while True:
    if jam_ganjil():
        video = ambil_video_belum_upload()
        if video:
            upload(video)
            # log
    time.sleep(60)
