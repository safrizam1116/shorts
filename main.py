import time
import datetime
import os
import json
import pytz
from threading import Thread
from flask import Flask

from downloader import download_from_gdrive
from cutter import cut_video
from auto_uploader import upload_video

# ==== KONFIGURASI ====
VIDEO_ID = "1i8iT8IR5nzVNcyLSaue1l5WWNkve0xiR"
INPUT_PATH = "input/video.mp4"
OUTPUT_PATH = "final/short.mp4"
UPLOAD_LOG = "logs/uploaded.json"
CLIP_DURATION = 27  # detik

# ==== WIB ====
def get_current_wib_time():
    utc_now = datetime.datetime.utcnow()
    wib_now = utc_now.replace(tzinfo=pytz.utc).astimezone(pytz.timezone("Asia/Jakarta"))
    return wib_now

def is_upload_time():
    now = get_current_wib_time()
    return now.hour % 2 == 1 and now.minute == 0

# ==== OFFSET ====
def get_last_offset():
    if not os.path.exists(UPLOAD_LOG):
        return 0
    with open(UPLOAD_LOG, "r") as f:
        data = json.load(f)
        return data.get("last_offset", 0)

def save_offset(offset):
    os.makedirs("logs", exist_ok=True)
    with open(UPLOAD_LOG, "w") as f:
        json.dump({"last_offset": offset}, f)

# ==== TUGAS UTAMA ====
def upload_task():
    now_str = get_current_wib_time().strftime('%Y-%m-%d %H:%M:%S')
    print(f"\n⏰ {now_str} WIB | Mulai upload...")

    try:
        os.makedirs("input", exist_ok=True)
        download_from_gdrive(VIDEO_ID, INPUT_PATH)

        offset = get_last_offset()
        start_time = offset * CLIP_DURATION

        cut_video(INPUT_PATH, OUTPUT_PATH, start_time=start_time, duration=CLIP_DURATION)

        upload_video(OUTPUT_PATH, title=f"🔥 Short Jedag Jedug", description="#shorts #viral")

        save_offset(offset + 1)
        print("✅ Upload sukses!")

    except Exception as e:
        print(f"❌ Gagal upload: {e}")

# ==== FAKE SERVER untuk Render ====
app = Flask(__name__)

@app.route('/')
def index():
    return "🟢 Bot aktif di Web Service Render.com"

def run_flask():
    app.run(host="0.0.0.0", port=3000)

# ==== MAIN ====
if __name__ == "__main__":
    # Jalankan Flask di thread terpisah
    Thread(target=run_flask).start()

    # Tunggu server hidup
    time.sleep(3)

    # Jalankan upload jika jam ganjil
    if is_upload_time():
        upload_task()
    else:
        print(f"⏳ Bukan jam ganjil WIB ({get_current_wib_time().strftime('%H:%M')}). Bot idle.")

    # Loop agar tidak mati
    while True:
        time.sleep(30)
