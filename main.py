import time
import datetime
import os
import json
from downloader import download_from_gdrive
from cutter import cut_video
from auto_uploader import upload_video

# ==== KONFIGURASI ====
VIDEO_ID = "1i8iT8IR5nzVNcyLSaue1l5WWNkve0xiR"
INPUT_PATH = "input/video.mp4"
OUTPUT_PATH = "final/short.mp4"
UPLOAD_LOG = "logs/uploaded.json"
CLIP_DURATION = 27  # detik

def is_odd_hour():
    now = datetime.datetime.now()
    return now.hour % 2 == 1

def has_uploaded_today():
    if not os.path.exists(UPLOAD_LOG):
        return False
    with open(UPLOAD_LOG, "r") as f:
        log = json.load(f)
    today = datetime.datetime.now().strftime("%Y-%m-%d-%H")
    return today in log

def save_upload_log():
    now_key = datetime.datetime.now().strftime("%Y-%m-%d-%H")
    os.makedirs("logs", exist_ok=True)
    if not os.path.exists(UPLOAD_LOG):
        with open(UPLOAD_LOG, "w") as f:
            json.dump([], f)
    with open(UPLOAD_LOG, "r+") as f:
        log = json.load(f)
        log.append(now_key)
        f.seek(0)
        json.dump(log, f)
        f.truncate()

def main():
    while True:
        now = datetime.datetime.now()
        print(f"⏰ Sekarang jam {now.strftime('%H:%M:%S')}")

        if is_odd_hour() and not has_uploaded_today():
            print("🚀 Proses upload dimulai...")

            try:
                # 1. Download
                os.makedirs("input", exist_ok=True)
                download_from_gdrive(VIDEO_ID, INPUT_PATH)

                # 2. Cut video
                cut_video(INPUT_PATH, OUTPUT_PATH, duration=CLIP_DURATION)

                # 3. Upload to YouTube
                upload_video(OUTPUT_PATH, title="🔥 Short Jedag Jedug", description="#shorts #viral")

                # 4. Simpan log
                save_upload_log()

                print("✅ Upload sukses.")

            except Exception as e:
                print(f"❌ Gagal upload: {e}")

        else:
            print("⏳ Belum jam ganjil atau sudah upload. Tidur dulu...")

        time.sleep(60 * 60)  # Tidur 1 jam

if __name__ == "__main__":
    main()
