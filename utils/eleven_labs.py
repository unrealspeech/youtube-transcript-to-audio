from elevenlabs import voices, generate, save, set_api_key
from dotenv import load_dotenv
import os

load_dotenv()


API_KEY = os.getenv("ELEVEN_LAB_API_KEY")
set_api_key(api_key=API_KEY)


audio_filename = 'audio.mp3'


def elevenlabs_voicer(text):
    audio = generate(text=text)
    save(audio, audio_filename)
