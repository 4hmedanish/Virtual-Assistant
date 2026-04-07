import os 
import random
from turtle import listen
import webbrowser
import pyautogui 
import pyttsx3
import speech_recognition as sr
import requests
from bs4 import BeautifulSoup
import datetime
import eel

# 🔥 INIT EEL
eel.init('web')

# TTS (you are using gTTS now)
from gtts import gTTS
import pygame
import time

pygame.mixer.init()

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
    pygame.mixer.music.unload()  

    time.sleep(0.2)  

    try:
        os.remove(filename)
    except:
        pass


def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        eel.updateStatus("Listening...")
        r.pause_threshold = 1
        r.energy_threshold = 300
        audio = r.listen(source, 0, 4)

    try:
        eel.updateStatus("Understanding...")
        query = r.recognize_google(audio, language='en-in')
        eel.updateStatus(f"You said: {query}")
    except Exception:
        eel.updateStatus("Say that again...")
        return "None"
    return query.lower()


# 🔥 EXPOSE TO JS
@eel.expose
def startListening():
    speak("Hello, how can I assist you today?")
    
    while True:
        query = takeCommand().lower()

        if "turn of" in query:
            speak("Ok sir , You can call me anytime")
            break

        elif "translate" in query:
            from Functions.Translator import translategl
            query = query.replace("translate","")
            translategl(query)
                    
        elif "hello" in query:
            speak("Hello sir, how are you ?")

        elif "i am fine" in query:
            speak("that's great, sir")

        elif "how are you" in query:
            speak("Perfect, sir")

        elif "thank you" in query:
            speak("you are welcome, sir")

        elif "shutdown the system" in query:
            speak("Shutting down the system...")
            os.system("shutdown /s /t 1")

        elif "open" in query:
            query = query.replace("open","")
            query = query.replace("jarvis","")
            pyautogui.press("super")
            pyautogui.typewrite(query)
            pyautogui.sleep(2)
            pyautogui.press("enter")
                
        elif "screenshot" in query:
            im = pyautogui.screenshot()
            im.save("ss.jpg")

        elif "click my photo" in query:
            pyautogui.press("super")
            pyautogui.typewrite("camera")
            pyautogui.press("enter")
            pyautogui.sleep(2)
            speak("SMILE")
            pyautogui.press("enter")

        elif "volume up" in query:
            from Functions.keyboard import volumeup
            speak("Turning volume up,sir")
            volumeup()

        elif "volume down" in query:
            from Functions.keyboard import volumedown
            speak("Turning volume down, sir")
            volumedown()

        elif "pause" in query:
            pyautogui.press("k")
            speak("video paused")

        elif "play" in query:
            pyautogui.press("k")
            speak("video played")

        elif "mute" in query:
            pyautogui.press("m")
            speak("video muted")

        elif "favourite" in query:
            speak("Playing your favourite songs, sir")
            a = (1,2,3)
            b = random.choice(a)
            if b==1:
                webbrowser.open("https://www.youtube.com/watch?v=6wrED1dw4Eo")
            elif b==2:
                webbrowser.open("https://www.youtube.com/watch?v=roz9sXFkTuE")
            elif b==3:
                webbrowser.open("https://www.youtube.com/watch?v=HPsxxBhv9kc")

        elif "open" in query:
            from Functions.Dictapp import openappweb
            openappweb(query)

        elif "close" in query:
            from Functions.Dictapp import closeappweb
            closeappweb(query)

        elif "google" in query:
            from Functions.SearchNow import searchGoogle
            searchGoogle(query)

        elif "youtube" in query:
            from Functions.SearchNow import searchYoutube
            searchYoutube(query)

        elif "wikipedia" in query:
            from Functions.SearchNow import searchWikipedia
            searchWikipedia(query)

        elif "calculate" in query:
            from Functions.Calculatenumbers import Calc
            query = query.replace("calculate","")
            query = query.replace("jarvis","")
            Calc(query)

        elif "temperature" in query or "weather" in query:
            search = "temperature in nagpur"
            url = f"https://www.google.com/search?q={search}"
            r = requests.get(url)
            data = BeautifulSoup(r.text,"html.parser")
            temp = data.find("div", class_="BNeawe")
            
            if temp:
                speak(f"Current {search} is {temp.text}")
            else:
                speak("Sorry, I couldn't fetch temperature")

        elif "remember that" in query:
            rememberMessage = query.replace("remember that","")
            speak("You told me to remember that " + rememberMessage)
            with open("Remember.txt","a") as remember:
                remember.write(rememberMessage + "\n")

        elif "what do you remember" in query:
            try:
                with open("Remember.txt","r") as remember:
                    speak("You told me to remember that " + remember.read())
            except:
                speak("I don't remember anything yet")

        elif "time" in query:
            strTime = datetime.datetime.now().strftime("%H:%M")    
            speak(f"Sir, the time is {strTime}")

        elif "sleep" in query:
            speak("Going to sleep,sir")
            exit()


# 🔥 START UI
eel.start('index.html', size=(700, 500))