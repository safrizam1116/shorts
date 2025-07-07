from moviepy.editor import VideoFileClip
import os

def cut_video(input_path, output_path, duration=27):
    print(f"✂️ Cutting {input_path} to {duration} seconds...")
    clip = VideoFileClip(input_path).subclip(0, duration)
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    clip.write_videofile(output_path, codec="libx264", audio_codec="aac")
    print(f"✅ Saved cut video to {output_path}")

# Contoh penggunaan langsung (optional untuk test)
if __name__ == "__main__":
    cut_video("input/video.mp4", "final/short.mp4", duration=27)
