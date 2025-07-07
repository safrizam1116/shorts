import requests
import os

def download_from_gdrive(file_id, destination_path):
    print(f"⬇️ Downloading from Google Drive: {file_id}")
    URL = "https://drive.google.com/uc?export=download"

    session = requests.Session()
    response = session.get(URL, params={"id": file_id}, stream=True)

    # Cek jika Google kasih token konfirmasi
    token = _get_confirm_token(response)
    if token:
        params = {"id": file_id, "confirm": token}
        response = session.get(URL, params=params, stream=True)

    _save_response_content(response, destination_path)
    print(f"✅ Saved to {destination_path}")

def _get_confirm_token(response):
    for key, value in response.cookies.items():
        if key.startswith("download_warning"):
            return value
    return None

def _save_response_content(response, destination):
    CHUNK_SIZE = 32768
    with open(destination, "wb") as f:
        for chunk in response.iter_content(CHUNK_SIZE):
            if chunk:
                f.write(chunk)

# Contoh penggunaan langsung (optional untuk test)
if __name__ == "__main__":
    FILE_ID = "1i8iT8IR5nzVNcyLSaue1l5WWNkve0xiR"
    OUTPUT = "input/video.mp4"
    os.makedirs("input", exist_ok=True)
    download_from_gdrive(FILE_ID, OUTPUT)
