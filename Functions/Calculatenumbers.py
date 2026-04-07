import wolframalpha
import pyttsx3
from gtts import gTTS
from playsound import playsound
import os
import speech_recognition
import eel

engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id)
rate = engine.setProperty("rate",170)

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

def WolfRamAlpha(query):
    apikey = "VQRRYV-WJ8UL76UQL"
    requester = wolframalpha.Client(apikey)
    requested = requester.query(query)

    try:
        answer = next(requested.results).text
        return answer
    except:
        speak("The value is not answerable")

def Calc(query):
    Term = str(query)
    Term = Term.replace("jarvis","")
    Term = Term.replace("into","*")
    Term = Term.replace("multiply","*")
    Term = Term.replace("plus","+")
    Term = Term.replace("minus","-")
    Term = Term.replace("divide","/")

    Final = str(Term)
    try:
        result = WolfRamAlpha(Final)
        print(f"{result}")
        speak(result)

    except:
        speak("The value is not answerable")