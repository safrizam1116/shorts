import subprocess

def cut_video(input_path, output_path, start_time=0, duration=27):
    print(f"✂️ Potong video mulai detik {start_time}")
    command = [
        "ffmpeg",
        "-y",
        "-ss", str(start_time),
        "-i", input_path,
        "-t", str(duration),
        "-c", "copy",
        output_path
    ]
    subprocess.run(command, check=True)
    print("✅ Video berhasil dipotong")
