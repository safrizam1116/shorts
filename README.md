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
bash
Copy
Edit

python split_and_effect.py

4. Jalankan bot upload otomatis (dengan upscale ke 2K):
bash
Copy
Edit

python auto_uploader.py

🔧 Ganti Durasi Shorts
Durasi default adalah 27 detik. Jika ingin mengubah:

Buka split_and_effect.py

Cari variabel ini:

python
Copy
Edit

SHORTS_DURATION = 27  # Ganti jadi 15, 30, atau 60 jika perlu

---
🌐 Jalankan 24 Jam Nonstop di Render
Fork repo ini ke GitHub kamu

Masuk ke Render.com

Pilih: New ➜ Web Service ➜ Hubungkan GitHub ➜ Repo ini

Render akan membaca render.yaml dan menjalankan bot secara otomatis
