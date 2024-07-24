from pydub import AudioSegment
import numpy as np
import requests
import tempfile
import os
import io

unreal_key = os.getenv("UNREAL_KEY")

def gen_unreal_audio(text: str, voice: str = "Scarlett") -> bytes | None:
    unreal_url = "https://api.v7.unrealspeech.com/stream"

    payload = {
        "Text": text,
        "VoiceId": voice,
        "Bitrate": "192k",
        "Speed": "0",
        "Pitch": "1",
        "Codec": "libmp3lame",
        "Temperature": 0.25
    }
    headers = {
        "accept": "text/plain",
        "content-type": "application/json",
        "Authorization": f"Bearer {unreal_key}"
    }

    response = requests.post(unreal_url, json=payload, headers=headers)

    if "ID3" not in str(response.content):
        print(f"\n{response.content}")
        return None

    return response.content

def concatenate_audios(audios: list[bytes]) -> np.ndarray:
    """
    Concatenate the audios of the list where isn't None.
    """
    concat_audio: AudioSegment = AudioSegment.from_file(io.BytesIO(audios[0]))
    for audio in audios[1:]:
        if audio is None: continue
        audio = AudioSegment.from_file(io.BytesIO(audio))
        concat_audio = concat_audio.append(audio)
    with tempfile.NamedTemporaryFile(delete=False) as temp_audio:
        concat_audio.export(temp_audio.name, format="mp3")
    return temp_audio.name

unreal_voices = ["Dan", "Scarlett", "Liv", "Will", "Amy"]
