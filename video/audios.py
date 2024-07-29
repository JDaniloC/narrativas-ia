import azure.cognitiveservices.speech as speechsdk
from moviepy.editor import AudioFileClip
from pydub import AudioSegment
import numpy as np
import requests
import tempfile
import os
import io

UNREAL_KEY = os.getenv("UNREAL_KEY")
SPEECH_KEY = os.environ.get("SPEECH_KEY")
SPEECH_REGION = os.environ.get("SPEECH_REGION")

def gen_unreal_audio(text: str, voice_key: str) -> bytes:
    unreal_url = "https://api.v7.unrealspeech.com/stream"
    voice = unreal_voices_map[voice_key]

    payload = {
        "Text": text,
        "VoiceId": voice,
        "Bitrate": "192k",
        "Speed": "0",
        "Pitch": "1" if voice != "Scarlett" else "1.5",
        "Codec": "libmp3lame",
        "Temperature": 0.25
    }
    headers = {
        "accept": "text/plain",
        "content-type": "application/json",
        "Authorization": f"Bearer {UNREAL_KEY}"
    }

    response = requests.post(unreal_url, json=payload, headers=headers)

    if "ID3" in str(response.content):
        return response.content

def gen_azure_audio(text: str, voice_key: str) -> bytes:
    """
    Generate an audio file from the given text using Azure Speech 
    Service and the selected voice. If the voice is not available
    in the Azure Speech Service, returns None.
    """
    speech_config = speechsdk.SpeechConfig(subscription=SPEECH_KEY,
                                           region=SPEECH_REGION)
    speech_config.speech_synthesis_voice_name = azure_voices_map[voice_key]
    speech_recognizer = speechsdk.SpeechSynthesizer(speech_config, None)

    result = speech_recognizer.speak_text_async(text).get()
    if result.reason == speechsdk.ResultReason.SynthesizingAudioCompleted:
        return result.audio_data

def concatenate_audios(audios: list[bytes]) -> str|None:
    """
    Concatenate the audios of the list where isn't None.
    Returns the path of the concatenated audio file.
    """
    if audios is None or len(audios) == 0: return
    first_audio = io.BytesIO(audios[0])
    concat_audio: AudioSegment = AudioSegment.from_file(first_audio)
    for audio in audios[1:]:
        if audio is None: continue
        audio = AudioSegment.from_file(io.BytesIO(audio))
        concat_audio = concat_audio.append(audio)
    with tempfile.NamedTemporaryFile(delete=False) as temp_audio:
        concat_audio.export(temp_audio.name, format="wav")
    return temp_audio.name

def get_duration(audio_path: np.ndarray) -> int:
    """
    Get the duration of the audio in seconds
    """
    return AudioFileClip(audio_path).duration

azure_voices_map = {
    "[BR] Adulto Donato": "pt-BR-DonatoNeural",
    "[BR] Adulto Antônio": "pt-BR-AntonioNeural",
    "[BR] Criança Letícia": "pt-BR-LeticiaNeural",
    "[BR] Jovem Yara": "pt-BR-YaraNeural",
    "[BR] Adulto Elza": "pt-BR-ElzaNeural",
    "[BR] Adulto Giovanna": "pt-BR-GiovannaNeural"
}

unreal_voices_map = {
    "[EN] Adult Dan": "Dan",
    "[EN] Old Will": "Will",
    "[EN] Adult Scarlett": "Scarlett",
    "[EN] Adult Liv": "Liv",
    "[EN] Adult Amy": "Amy"
}

unreal_voices = list(unreal_voices_map.keys())
azure_voices = list(azure_voices_map.keys())

voice_mapping = unreal_voices + azure_voices