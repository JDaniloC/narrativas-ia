from moviepy.editor import (VideoFileClip, AudioFileClip, CompositeAudioClip,
                            concatenate_videoclips,
                            concatenate_audioclips)
from os import listdir

def get_number(file_name: str):
    if not file_name.startswith("."):
        page = file_name.split("_")[-1]
        return int(page.split(".")[0])
    return 0

RESOLUTION = (1080, 1920)

audios = list()
for audio in sorted(listdir('./audios'), key=get_number):
    audios.append(AudioFileClip(f'./audios/{audio}'))
audios = concatenate_audioclips(audios).volumex(0.1)

clips = list()
videos = listdir('./videos')
for video in sorted(videos, key=get_number):
    if not video.startswith("."):
        video_path = f'./videos/{video}'
        clip = VideoFileClip(video_path, target_resolution=RESOLUTION)
        clips.append(clip)

final_clip = concatenate_videoclips(clips)
audio = CompositeAudioClip([final_clip.audio,
                            audios.set_duration(final_clip.duration)])

final_clip = final_clip.set_audio(audio)
final_clip.write_videofile("final_movie.mp4")

