import pyttsx3
import datetime
from gtts import gTTS
from playsound import playsound
import os
import eel

engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id)
engine.setProperty("rate",200)

import pygame
import time
import uuid

pygame.mixer.init()

def speak(audio):
    print(f"Assistant: {audio}")
    eel.updateStatus(f"Assistant: {audio}")

    # 🔥 unique filename (avoids lock issue)
    filename = f"voice_{uuid.uuid4().hex}.mp3"

    tts = gTTS(text=audio, lang='en')
    tts.save(filename)

    pygame.mixer.music.load(filename)
    pygame.mixer.music.play()

    while pygame.mixer.music.get_busy():
        time.sleep(0.1)

    pygame.mixer.music.stop()
    pygame.mixer.music.unload()   # 🔥 VERY IMPORTANT

    time.sleep(0.2)  # 🔥 allow Windows to release file

    try:
        os.remove(filename)
    except:
        pass

def greetMe():
    hour  = int(datetime.datetime.now().hour)
    if hour>=0 and hour<=12:
        speak("Good Morning,sir")
    elif hour >12 and hour<=18:
        speak("Good Afternoon ,sir")

    else:
        speak("Good Evening,sir")

    speak("Please tell me, How can I help you ?")