📩 Contact
Created by : Safri Rafiq
Licence    : Contact me directly
📧 Email   : safrizam07@gmail.com

# 🎬 YouTube Shorts Auto Uploader Bot

This bot automates the entire process of publishing YouTube Shorts. It:

- ✂️ Cuts long videos into clean **27-second** segments
- 💥 Adds simple **"jedag-jedug"** effects (zoom + contrast)
- 📈 Upscales each video to **2K resolution (2560×1440)**
- 📤 Uploads to YouTube Shorts automatically on **odd-numbered hours** (1 AM, 3 AM, 5 AM…)
- 🔁 Runs continuously, 24/7 — perfect for content farming or automation

---

## 📂 Folder Structure

/
├── input/ # Raw videos (from Google Drive or local)
├── output/ # After splitting and applying effects
├── upscale/ # 2K versions ready for upload
├── logs/uploaded.json # Log of uploaded files (avoid duplicates)
├── auto_uploader.py # Main uploader script (with upscale)
├── split_and_effect.py # Cuts & adds effects
├── ffmpeg_upscale.py # Upscales videos to 2K
├── credentials.json # Google API OAuth2 (REQUIRED)
├── requirements.txt # Dependencies list
├── render.yaml # (Optional) Auto-deploy to Render
├── README.md # You're reading this!

---

## 🚀 How to Run the Bot

### 1. Install the dependencies:

```bash
pip install -r requirements.txt

2. Put your source video inside the input/ folder
(You can also fetch videos from Google Drive using an optional script)

3. Run the splitter + effect processor (cuts into 27-second clips):
python split_and_effect.py

4. Run the auto-upload bot (with 2K upscale):
python auto_uploader.py

⚙️ Change Shorts Duration?
The default segment length is 27 seconds.
To change it:

Open split_and_effect.py

Find this line:

SHORTS_DURATION = 27  # Change to 15, 30, or 60 as needed

☁️ Deploy to Render (24/7 Automation)
Want this bot to run non-stop in the cloud?

Fork this repo to your GitHub

Go to Render.com

Choose: New ➜ Web Service ➜ Connect to your repo

Render will detect render.yaml and auto-deploy the bot

---

🔐 Setting up credentials.json (OAuth2 for YouTube API)
Go to Google Cloud Console

Create a new project

Enable YouTube Data API v3

Open OAuth Consent Screen → choose External, fill in required fields

Go to Credentials → Create Credentials → OAuth Client ID

App type: Desktop App

Download the .json and rename it to credentials.json

Place it in your project root folder

✅ The first time you run the bot, a browser will open asking you to sign in. Once you do, your token will be saved.

🧠 Upload Log
Every video that gets uploaded is automatically logged in:

logs/uploaded.json
This prevents the bot from uploading the same video twice.

------------------------------------------------------------------------------------------------------------------------

📩 Kontak
Dibuat oleh : Safri Rafiq
Lisensi     : hubungi saya langsung.
email       : safrizam07@gmail.com

# 🎬 YouTube Shorts Auto Uploader Bot

Bot ini otomatis:
- 🧠 Memotong video panjang jadi potongan pendek **27 detik**
- 💥 Menambahkan efek **jedag-jedug** (zoom + kontras)
- 🔼 Mengubah resolusi ke **2K (2560x1440)** sebelum upload
- 📤 Upload ke YouTube Shorts **setiap jam ganjil (1, 3, 5, ..., 23)**
- 🔁 Jalan terus 24 jam nonstop (loop terjadwal)

---

## 📂 Struktur Folder

/
├── input/ # Video mentah (dari Google Drive atau lokal)
├── output/ # Video setelah dipotong & diberi efek
├── upscale/ # Video 2K hasil upscale sebelum upload
├── logs/uploaded.json # Log video yang sudah diupload
├── auto_uploader.py # Script utama upload + 2K
├── split_and_effect.py # Potong video + efek jedag
├── ffmpeg_upscale.py # Script upscale ke 2K
├── credentials.json # File auth Google API (WAJIB)
├── requirements.txt # Dependensi
├── render.yaml # (Opsional) Auto-deploy ke Render
├── README.md # Dokumentasi ini

---

## 🛠️ Cara Jalankan Bot Upload Shorts

### 1. Install dependensi:

```bash
pip install -r requirements.txt

2. Masukkan video ke folder input/
Bisa juga dari Google Drive, nanti pakai downloader tambahan (opsional)

3. Jalankan proses split + efek (durasi 27 detik per potong):

python split_and_effect.py

4. Jalankan bot upload otomatis (dengan upscale ke 2K):

python auto_uploader.py

🔧 Ganti Durasi Shorts
Durasi default adalah 27 detik. Jika ingin mengubah:

Buka split_and_effect.py

Cari variabel ini:

SHORTS_DURATION = 27  # Ganti jadi 15, 30, atau 60 jika perlu

---
🌐 Jalankan 24 Jam Nonstop di Render
Fork repo ini ke GitHub kamu

Masuk ke Render.com

Pilih: New ➜ Web Service ➜ Hubungkan GitHub ➜ Repo ini

Render akan membaca render.yaml dan menjalankan bot secara otomatis

🔑 Setup Google API: credentials.json
Buka Google Cloud Console

Buat Project baru

Aktifkan YouTube Data API v3

Masuk ke OAuth Consent Screen ➜ pilih External ➜ isi data (nama, dll)

Buat OAuth 2.0 Client ID

Application type: Desktop

Download file .json ➜ rename jadi:
credentials.json
Letakkan di folder utama project ini

✅ Pertama Kali Jalan
Saat pertama kali upload, bot akan:

Munculkan browser popup untuk login Google

Kamu login dan beri izin ➜ akan tersimpan di auth_token.json

🧠 Log Upload
Semua video yang sudah diupload akan dicatat di:

logs/uploaded.json

Agar tidak dobel upload.

