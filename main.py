import os
import json
import time
import datetime
import pytz
from flask import Flask
from threading import Thread

from downloader import download_from_gdrive
from cutter import cut_video
from auto_uploader import upload_video

# === KONFIGURASI ===
VIDEO_ID = "1i8iT8IR5nzVNcyLSaue1l5WWNkve0xiR"
INPUT_PATH = "input/video.mp4"
OUTPUT_PATH = "final/short.mp4"
UPLOAD_LOG = "logs/uploaded.json"
CLIP_DURATION = 27  # detik

app = Flask(__name__)
status = {"last_upload": "-", "status": "Bot aktif, belum upload"}

# === WIB TIME ===
def get_current_wib_time():
    utc_now = datetime.datetime.utcnow()
    wib = utc_now.replace(tzinfo=pytz.utc).astimezone(pytz.timezone("Asia/Jakarta"))
    return wib

# === CEK JAM GANJIL ===
def is_upload_time():
    now = get_current_wib_time()
    return now.hour % 2 == 1 and now.minute == 0

# === OFFSET CLIP ===
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

# === UPLOAD TASK ===
def upload_task():
    try:
        print(f"⏰ {get_current_wib_time().strftime('%H:%M:%S')} WIB | Mulai upload...")
        os.makedirs("input", exist_ok=True)
        download_from_gdrive(VIDEO_ID, INPUT_PATH)

        offset = get_last_offset()
        start_time = offset * CLIP_DURATION

        cut_video(INPUT_PATH, OUTPUT_PATH, start_time=start_time, duration=CLIP_DURATION)
        upload_video(OUTPUT_PATH, title="🔥 Short Jedag Jedug", description="#shorts #viral")

        save_offset(offset + 1)
        status["status"] = "✅ Upload sukses"
        status["last_upload"] = get_current_wib_time().strftime("%Y-%m-%d %H:%M:%S")

        print("✅ Upload selesai!")

    except Exception as e:
        status["status"] = f"❌ Gagal upload: {str(e)}"
        print(f"❌ Gagal upload: {e}")

# === FLASK APP UNTUK RENDER.COM ===
@app.route('/')
def home():
    return f"""
    <h3>🟢 Bot Shorts Aktif</h3>
    <p>Status: {status["status"]}</p>
    <p>Last Upload: {status["last_upload"]}</p>
    <p>Time (WIB): {get_current_wib_time().strftime("%Y-%m-%d %H:%M:%S")}</p>
    """

def run_flask():
    app.run(host="0.0.0.0", port=3000)

# === MAIN LOOP ===
def bot_loop():
    while True:
        if is_upload_time():
            upload_task()
            time.sleep(65)  # tunggu lewat 1 menit agar tidak dobel
        else:
            print(f"⏳ {get_current_wib_time().strftime('%H:%M:%S')} WIB | Bukan jam ganjil.")
            time.sleep(30)

if __name__ == "__main__":
    print("🚀 Bot Shorts Render Web Service dimulai...")
    Thread(target=run_flask).start()
    time.sleep(2)
    bot_loop()
