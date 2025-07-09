import os
import time
import json
from datetime import datetime
from ffmpeg_upscale import upscale_to_2k
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload
from oauth2client.file import Storage
from oauth2client.tools import run_flow
from oauth2client.client import flow_from_clientsecrets
from dotenv import load_dotenv

# ======================
# LOAD ENV
# ======================

load_dotenv()
CLIENT_SECRET = os.getenv("CLIENT_SECRET", "/etc/secrets/credentials.json")
TOKEN_PATH = os.getenv("TOKEN_PATH", "/etc/secrets/auth_token.json")

# ======================
# CONFIG
# ======================

OUTPUT_FOLDER = 'output'
UPSCALE_FOLDER = 'upscale'
LOG_FILE = 'logs/uploaded.json'

os.makedirs(UPSCALE_FOLDER, exist_ok=True)
os.makedirs('logs', exist_ok=True)

# ======================
# YOUTUBE AUTH
# ======================

def get_authenticated_service():
    storage = Storage(TOKEN_PATH)
    credentials = storage.get()

    if not credentials or credentials.invalid:
        flow = flow_from_clientsecrets(CLIENT_SECRET, scope="https://www.googleapis.com/auth/youtube.upload")
        credentials = run_flow(flow, storage)

    return build('youtube', 'v3', credentials=credentials)

youtube = get_authenticated_service()

# ======================
# LOGIC
# ======================

def jam_ganjil():
    now = datetime.now()
    return now.hour % 2 == 1 and now.minute == 0

def load_log():
    if not os.path.exists(LOG_FILE):
        return []
    with open(LOG_FILE, 'r') as f:
        return json.load(f)

def save_log(log):
    with open(LOG_FILE, 'w') as f:
        json.dump(log, f, indent=2)

def ambil_video_baru():
    uploaded = load_log()
    for f in sorted(os.listdir(OUTPUT_FOLDER)):
        if f.endswith('.mp4') and f not in uploaded:
            return f
    return None

def upload_video(file_path, title="My Shorts"):
    media = MediaFileUpload(file_path, chunksize=-1, resumable=True, mimetype='video/*')
    request = youtube.videos().insert(
        part="snippet,status",
        body={
            "snippet": {
                "title": title,
                "description": "#shorts",
                "tags": ["shorts", "viral"],
                "categoryId": "22"
            },
            "status": {
                "privacyStatus": "public"
            }
        },
        media_body=media
    )
    response = None
    while response is None:
        status, response = request.next_chunk()
        if status:
            print(f"📤 Uploading: {int(status.progress() * 100)}%")
    print(f"✅ Upload selesai → https://youtube.com/watch?v={response['id']}")

# ======================
# MAIN LOOP
# ======================

print("🟢 Bot upload Shorts 2K aktif...")

while True:
    now = datetime.now()
    if jam_ganjil():
        video_name = ambil_video_baru()
        if video_name:
            print(f"[{now}] 🎞 Menemukan video: {video_name}")

            input_path = os.path.join(OUTPUT_FOLDER, video_name)
            output_path = os.path.join(UPSCALE_FOLDER, video_name)

            print("🔧 Upscaling ke 2K...")
            upscale_to_2k(input_path, output_path)

            print("📤 Uploading ke YouTube...")
            upload_video(output_path, title=f"🔥 Shorts {now.strftime('%H:%M')}")

            log = load_log()
            log.append(video_name)
            save_log(log)
            print("✅ Selesai. Menunggu jam ganjil berikutnya.")
        else:
            print(f"[{now}] ⚠️ Tidak ada video baru.")
        time.sleep(3600)
    else:
        print(f"[{now}] ⏳ Bukan jam ganjil. Tidur 1 menit...")
        time.sleep(60)
