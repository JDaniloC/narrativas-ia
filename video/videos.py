from moviepy.editor import (VideoFileClip, AudioFileClip, CompositeAudioClip,
                            concatenate_videoclips, concatenate_audioclips,
                            AudioClip)
import tempfile

RESOLUTION = (1080, 1920)

def add_audio_to_video(video_path: str|None, audio_path: str|None,
                       video_list: list[str]) -> tuple[str, list[str]]:
    """
    Add audio to the given video file and save it in a temporary file.
    Returns the name of the temporary file and adds it to the video_list.
    """
    if video_path is None: return None, video_list
    if audio_path is None:
        video_list.append(video_path)
        return video_path, video_list

    clip = VideoFileClip(video_path, target_resolution=RESOLUTION)
    audio = AudioFileClip(audio_path)
    blank = AudioClip(make_frame=lambda t: 0, duration=0.5)
    audio = concatenate_audioclips((blank, audio, blank))
    clip: VideoFileClip = clip.set_audio(audio)

    with tempfile.NamedTemporaryFile(delete=False) as temp_video:
        video_name = temp_video.name + ".mp4"
        clip.write_videofile(video_name)
    video_list.append(video_name)
    return video_name, video_list

def join_videos(video_paths: list[str], bg_sound_paths: list[str]):
    """
    Join the videos in the list and add the audio to the final video.
    The sound will be concatenated and added to the final video with
    a volume of 10% and the video will be saved in a temporary file.
    """
    if len(video_paths) == 0: return

    clips = list()
    for video in video_paths:
        clips.append(VideoFileClip(video, target_resolution=RESOLUTION))

    audios = list()
    for audio in bg_sound_paths:
        if audio: audios.append(AudioFileClip(audio))

    final_clip = concatenate_videoclips(clips)
    if len(audios) > 0:
        final_audio = concatenate_audioclips(audios).volumex(0.1)
        final_audio = final_audio.set_duration(final_clip.duration)
        final_audio = CompositeAudioClip([final_clip.audio, final_audio])
        final_clip = final_clip.set_audio(final_audio)

    with tempfile.NamedTemporaryFile(delete=False) as temp_video:
        video_name = temp_video.name + ".mp4"
        final_clip.write_videofile(video_name)
    return video_name
