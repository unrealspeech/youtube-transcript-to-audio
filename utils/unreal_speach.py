from unrealspeech import UnrealSpeechAPI, play, save
from dotenv import load_dotenv
import os

load_dotenv()

api_key = os.getenv('UNREAL_SPEECH_API_KEY')

print(api_key)
speech_api = UnrealSpeechAPI(api_key)

audio_filename = 'audio.mp3'


def unrealspeech_voice(text):
    print(text)
    timestamp_type = "sentence"
    voice_id = "Will"
    task_id = speech_api.create_synthesis_task(
        text=text, voice_id=voice_id, timestamp_type=timestamp_type,)
    audio_data = speech_api.get_synthesis_task_status(task_id)

    # Play audio
    save(audio_data, audio_filename)
