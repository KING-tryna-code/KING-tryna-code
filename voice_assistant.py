import pyttsx3 #pip install pyttsx3
import speech_recognition as sr #pip install speechRecognition
import datetime
import wikipedia #pip install wikipedia
import webbrowser
import os
import smtplib

engine = pyttsx3.init()

def speak(audio):
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')  # getting details of current voice
    engine.setProperty('voice', voices[0].id)
    engine.say(audio)
    engine.runAndWait()
def wish_me():
    hour = int(datetime.datetime.now().hour)
    if hour>=21 or hour<=6:
        speak("good night")
    elif hour >6 and hour<=12:
        speak("good morning")
    elif hour >12 and hour<=18:
        speak("good evening")
    else :
        speak("time errror")
        print(hour)
def recog():
    with sr.Microphone() as source:
        with sr.Microphone() as source:
            r = sr.Recognizer()

            speak("Say something")
            print("listening.....")

            audio = r.listen(source)
            try:
                query = r.recognize_google(audio, language='en-in')
                r.energy_threshold=1
                speak(query)
                print("user said:",query)

            except Exception as e:

                speak("Say that again please...")
                return "none"
            return query
wish_me()
if __name__=="__main__" :

    query = recog().lower()

    if "open google" in query:
        url= "www.google.com"
        webbrowser.open(url)

    elif "open youtube" in  query:
        url= "www.youtube.com"
        webbrowser.open(url)
'''
    elif "wikipedia" in query:
        query = query.replace("wikipedia", "")
        results=wikipedia.summary(query, sentences=2)
        speak(results)
        print(results)
'''