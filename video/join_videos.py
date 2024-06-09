from moviepy.editor import VideoFileClip, concatenate_videoclips
from os import listdir

get_number_func = lambda x: int(x.split("_")[1].split(".")[0])

clips = list()
videos = listdir('./videos')
for video in sorted(videos, key=get_number_func):
    clips.append(VideoFileClip(f'./videos/{video}',
                               target_resolution=(1080, 1920)))

final_clip = concatenate_videoclips(clips)
final_clip.write_videofile("final_movie.mp4")
