from moviepy.editor import (ImageClip, CompositeVideoClip,
                            AudioFileClip, AudioClip,
                            concatenate_audioclips)
from os import listdir, path
import numpy as np

def get_number(file_name: str):
    if not file_name.startswith("."):
        page = file_name.split("_")[-1]
        return int(page.split(".")[0])
    return 0

def to_rgb(image: ImageClip):
    return np.dstack(3 * [1 * image]).astype('uint8')

def create_video(file_name: str, image_path: str, audio_path: str | None):
    audio = None
    duration = 7
    if audio_path is not None:
        audio = AudioFileClip(audio_path)
        blank = AudioClip(make_frame=lambda t: 0, duration=0.5)
        audio = concatenate_audioclips((blank, audio, blank))
        duration = max(audio.duration + 1, 5)

    clip = ImageClip(image_path, transparent=False)
    if len(clip.img.shape) == 2:
        clip = clip.fl_image(to_rgb)

    height_ratio = 1080 / 1920

    width, height = clip.size
    new_height = int(width * height_ratio)
    screensize = (width, new_height)

    y_speed = (height - new_height) / duration
    clip: ImageClip = clip.resize(height=screensize[1] * 4).set_duration(duration)

    clip = (
        CompositeVideoClip([clip])
        .resize(width=screensize[0])
        .set_position(lambda t: ("center", 1 - t * y_speed))
    )

    clip = CompositeVideoClip([clip], size=screensize)
    if audio_path is not None: clip = clip.set_audio(audio)

    clip.write_videofile(file_name, fps=24)


IMAGE_SUFFIX = ".jpg"
AUDIO_SUFFIX = ".mp3"
AUDIO_PREFIX = "audio_"

ASSETS_FOLDER = "./assets"
VIDEOS_FOLDER = "./videos"

assets = listdir(ASSETS_FOLDER)
for file_name in sorted(assets, key=get_number):
    if file_name.endswith(IMAGE_SUFFIX):
        audio_file_name = AUDIO_PREFIX + file_name.replace(IMAGE_SUFFIX,
                                                           AUDIO_SUFFIX)
        audio_path = f"{ASSETS_FOLDER}/{audio_file_name}"
        image_path = f"{ASSETS_FOLDER}/{file_name}"
        if not path.exists(audio_path): audio_path = None

        name = file_name.replace(IMAGE_SUFFIX, "")
        video_file_path = f"{VIDEOS_FOLDER}/{name}.mp4"
        if not path.exists(video_file_path):
            create_video(video_file_path, image_path, audio_path)
