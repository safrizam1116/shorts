import ffmpeg
import os

def upscale_to_2k(input_path, output_path):
    if not os.path.exists(output_path):
        (
            ffmpeg
            .input(input_path)
            .output(output_path, vf="scale=2560:1440", vcodec='libx264', crf=22, preset='slow')
            .run()
        )
