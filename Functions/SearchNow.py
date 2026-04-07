import speech_recognition
import pyttsx3
import pywhatkit
import wikipedia
import webbrowser
from gtts import gTTS
from playsound import playsound
import os
import eel


def takeCommand():
    r = speech_recognition.Recognizer()
    with speech_recognition.Microphone() as source:
        print("Listening.....")
        r.pause_threshold = 1
        r.energy_threshold = 300
        audio = r.listen(source,0,4)
    try:
        print("Understanding..")
        query  = r.recognize_google(audio,language='en-in')
        print(f"You Said: {query}\n")
    except Exception as e:
        print("Say that again")
        return "None"
    return query

query = takeCommand().lower()

engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id)
engine.setProperty("rate",170)

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

def searchGoogle(query):
    if "google" in query:
        import wikipedia as googleScrap
        query = query.replace("jarvis","")
        query = query.replace("google search","")
        query = query.replace("google","")
        query = query.replace("search","")
        query = query.replace("on","")
        speak("This is what I found on google")

        try:
            pywhatkit.search(query)
            result = googleScrap.summary(query,1)
            speak(result)

        except:
            speak("No speakable output available")

def searchYoutube(query):
    if "on youtube" in query:
        speak("This is what I found for your search!") 
        query = query.replace("youtube search","")
        query = query.replace("on youtube","")
        query = query.replace("search","")
        query = query.replace("youtube","")
        query = query.replace("play","")
        query = query.replace("jarvis","")
        web  = "https://www.youtube.com/results?search_query=" + query
        webbrowser.open(web)
        pywhatkit.playonyt(query)
        speak("Done, Sir")

def searchWikipedia(query):
    if "wikipedia" in query:
        speak("Searching from wikipedia....")
        query = query.replace("wikipedia","")
        query = query.replace("search","")
        query = query.replace("on wikipedia","")
        query = query.replace("search wikipedia","")
        query = query.replace("search","")
        query = query.replace("jarvis","")
        results = wikipedia.summary(query,sentences = 2)
        speak("According to wikipedia..")
        print(results)
        speak(results)

