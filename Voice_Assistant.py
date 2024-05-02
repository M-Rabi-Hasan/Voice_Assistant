import pyttsx3      # The pyttsx3 module is a text-to-speech (TTS) conversion library in Python. 
import speech_recognition as sr     # The speech_recognition module in Python provides functionality for speech recognition.
import webbrowser
import datetime                     # I -> houre, M -> minute, p -> am or pm
import pyjokes
import pyaudio
import os
import time

def sptext():
    recognizer = sr.Recognizer()  # sr -> Module , Recognizer -> Class
    while True:
        with sr.Microphone() as source:
            print("Listening...")
            recognizer.adjust_for_ambient_noise(source)         # for neglected noice
            audio = recognizer.listen(source)
            try:
                print("Recognizing....")
                data = recognizer.recognize_google(audio)
                print(data)
                return data
            except sr.UnknownValueError:
                print("Not understood")   # yahan tak hum ne speech to text kia hai
                continue

def speechtx(x):
    enging = pyttsx3.init()
    voice = enging.getProperty('voices')
    enging.setProperty('voice',voice[0].id)
    rate = enging.getProperty('rate')
    enging.setProperty('rate', 100)
    enging.say(x)
    enging.runAndWait()



if __name__ == '__main__':

    # if "hey peter" in sptext().lower():
        while True:
            data1 = sptext().lower()    # speech to text
            if "your name" in data1:
                name = "my name is peter"
                speechtx(name)              # text to speech
            elif "old are you" in data1:
                age = "my age is 26"
                speechtx(age)              # text to speech
            elif "who are you" in data1:
                know = "i am google assistant"
                speechtx(know)              # text to speech
            elif "time" in data1:
                time = datetime.datetime.now().strftime("%I%M%p")   # datetime.datetime -> module.function:  I -> houre, M -> minute, p -> am or pm
                speechtx(time)              # text to speech
            elif "youtube" in data1:
                webbrowser.open("https://www.youtube.com/")
            elif "joke" in data1:
                joke = pyjokes.get_joke(language="en", category="neutral")
                print(joke)
                speechtx(joke)              # text to speech
            elif "play song" in data1:
                add = "D:\song"
                listsong = os.listdir(add)
                print(listsong)
                os.startfile(os.path.join(add,listsong[0]))
            elif "exit" in data1:
                speechtx("Thank you")
                break
            time.sleep(1)
    # else:
    #     speechtx("Thanks")