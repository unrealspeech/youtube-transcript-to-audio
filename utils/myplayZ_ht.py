import requests
import os
from dotenv import load_dotenv

load_dotenv()


def playht_voice(text):
    url = "https://api.play.ht/api/v2/tts"

    payload = {
        "text": text,
        "voice": "s3://voice-cloning-zero-shot/d9ff78ba-d016-47f6-b0ef-dd630f59414e/female-cs/manifest.json",
        "output_format": "mp3",
        "voice_engine": "PlayHT2.0"
    }
    headers = {
        "accept": "text/event-stream",
        "content-type": "application/json",
        "AUTHORIZATION": os.getenv("PLAY_HT_API_KEY"),
        "X-USER-ID": os.getenv("PLAY_HT_USER_ID")
    }

    response = requests.post(url, json=payload, headers=headers)

    if response.status_code == 200:
        response_data = response.json()
        if response_data.get("url"):
            audio_url = response_data["url"]
            audio_response = requests.get(audio_url)

            if audio_response.status_code == 200:
                with open('audio.mp3', 'wb') as audio_file:
                    audio_file.write(audio_response.content)
                print("Audio file downloaded successfully.")
            else:
                print("Failed to download the audio file.")
        else:
            print("Audio URL not found in response.")
    else:
        print("Failed to generate audio. Status code:", response.status_code)


# Example usage
playht_voice("Hello from a realistic voice.")
