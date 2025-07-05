from moviepy.editor import VideoFileClip, concatenate_videoclips, vfx
import os

def potong_video(source):
    video = VideoFileClip(source)
    duration = video.duration
    count = int(duration // 10)
    
    for i in range(count):
        clip = video.subclip(i * 10, (i + 1) * 10)
        clip = clip.fx(vfx.lum_contrast, 0, 150, 255)  # optional efek
        clip = clip.fx(vfx.zoom_in, 1.05)  # zoom jedag
        filename = f"output/short_{i+1}.mp4"
        clip.write_videofile(filename)
