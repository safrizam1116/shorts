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
CLIP_DURATION = 27  # durasi Shorts (detik)

# ==== SERVER FLASK ====
app = Flask(__name__)

@app.route("/")
def index():
    return "✅ Bot Shorts aktif - Render.com"

def run_flask():
    port = int(os.environ.get("PORT", 3000))  # WAJIB agar Render mendeteksi
    app.run(host="0.0.0.0", port=port)

# ==== WAKTU WIB ====
def get_current_wib_time():
    utc_now = datetime.datetime.utcnow()
    return utc_now.replace(tzinfo=pytz.utc).astimezone(pytz.timezone("Asia/Jakarta"))

def is_upload_time():
    now = get_current_wib_time()
    return now.hour % 2 == 1 and now.minute == 0  # jam ganjil, menit ke-00

# ==== OFFSET LOGIC ====
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

# ==== PROSES UTAMA ====
def upload_task():
    now = get_current_wib_time()
    print(f"\n⏰ {now.strftime('%Y-%m-%d %H:%M:%S')} WIB | Mulai upload...")

    try:
        os.makedirs("input", exist_ok=True)
        download_from_gdrive(VIDEO_ID, INPUT_PATH)

        offset = get_last_offset()
        start_time = offset * CLIP_DURATION

        cut_video(INPUT_PATH, OUTPUT_PATH, start_time=start_time, duration=CLIP_DURATION)

        upload_video(OUTPUT_PATH, title="🔥 Short Jedag Jedug", description="#shorts #viral")

        save_offset(offset + 1)
        print("✅ Upload sukses!")

    except Exception as e:
        print(f"❌ Gagal upload: {e}")

# ==== MAIN ====
if __name__ == "__main__":
    Thread(target=run_flask).start()  # server Flask agar Render tetap ON
    time.sleep(3)  # tunggu server siap

    if is_upload_time():
        upload_task()
    else:
        now = get_current_wib_time()
        print(f"⏳ Bukan jam ganjil WIB, sekarang {now.strftime('%H:%M')}. Bot selesai.")

    # Keep-alive loop agar service tetap ON
    while True:
        time.sleep(30)
