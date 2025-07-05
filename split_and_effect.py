from moviepy.editor import VideoFileClip, vfx
import os

SHORTS_DURATION = 27
INPUT_FOLDER = 'input'
OUTPUT_FOLDER = 'output'

os.makedirs(OUTPUT_FOLDER, exist_ok=True)

def process_video(source):
    video = VideoFileClip(source)
    total = int(video.duration)
    parts = total // SHORTS_DURATION

    for i in range(parts):
        st = i * SHORTS_DURATION
        ed = st + SHORTS_DURATION
        clip = video.subclip(st, ed)
        clip = clip.fx(vfx.lum_contrast, 0, 150, 255) \
                   .fx(vfx.zoom_in, 1.05)
        filename = f"output/short_{i+1:02d}.mp4"
        clip.write_videofile(filename, codec="libx264", audio_codec="aac")
