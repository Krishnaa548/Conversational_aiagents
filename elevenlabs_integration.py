https://elevenlabs.io/app/talk-to?agent_id=0xAzvpW79PqQpFQ7pXyY
this is link of my agent


#code 
import os
import requests

ELEVEN_API_KEY = os.getenv("ELEVEN_API_KEY")  # Use GitHub Secrets for security
VOICE_ID = "21m00Tcm4TlvDq8ikWAM"  # Example voice ID (replace with yours)

def text_to_speech(text):
    url = f"https://api.elevenlabs.io/v1/text-to-speech/{VOICE_ID}/stream"
    headers = {"xi-api-key": ELEVEN_API_KEY}
    data = {
        "text": text,
        "voice_settings": {"stability": 0.5, "similarity_boost": 0.5}
    }
    response = requests.post(url, json=data, headers=headers, stream=True)
    return response.content  # Returns audio bytes for playback
