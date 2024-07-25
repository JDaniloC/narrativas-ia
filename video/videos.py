from moviepy.editor import (VideoFileClip, AudioFileClip,
                            concatenate_videoclips,
                            concatenate_audioclips)
import tempfile

RESOLUTION = (1080, 1920)

def add_audio_to_video(video_path: str, audio_path: str):
    """
    Add audio to the given video file and save it in a temporary file.
    """
    clip = VideoFileClip(video_path, target_resolution=RESOLUTION)
    clip: VideoFileClip = clip.set_audio(AudioFileClip(audio_path))
    with tempfile.NamedTemporaryFile(delete=False) as temp_video:
        video_name = temp_video.name + ".mp4"
        clip.write_videofile(video_name)
    return video_name

def join_videos(video_paths: list[str], bg_sound_paths: list[str]):
    """
    Join the videos in the list and add the audio to the final video.
    The sound will be concatenated and added to the final video with
    a volume of 10% and the video will be saved in a temporary file.
    """
    clips = list()
    for video in video_paths:
        clips.append(VideoFileClip(video, target_resolution=RESOLUTION))

    audios = list()
    for audio in bg_sound_paths:
        audios.append(AudioFileClip(audio))

    final_audio = concatenate_audioclips(audios).volumex(0.1)
    final_clip = concatenate_videoclips(clips)

    final_clip.set_audio(final_audio)
    with tempfile.NamedTemporaryFile(delete=False) as temp_video:
        video_name = temp_video.name + ".mp4"
        final_clip.write_videofile(video_name)
    return video_name
