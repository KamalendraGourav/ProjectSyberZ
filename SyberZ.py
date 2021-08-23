
import subprocess
import pyttsx3
import tkinter
import random
import operator
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import winshell
import pyjokes
import feedparser
import ctypes
import time
import requests
import shutil
from clint.textui import progress
from bs4 import BeautifulSoup
import win32com.client as wincl
from urllib.request import urlopen




engine = pyttsx3.init('sapi5') # sapi5 is microsoft API used for speech function
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id) # voice id "1 " for female voice

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def WishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning Master!")
    
    elif hour >=12 and hour<18:
        speak("Good Afternoon master !")
    
    else :
        speak("Good Evening master !")

    asn = (" I am Veronica , your friend and assistant")
    speak(asn)

def user():
    speak("what should i call you ")
    usern = takeCommand()
    speak(f"Welcome {usern}")

    speak("what can i help you ")

def takeCommand():

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening ...")
        r.pause_threshold = 1
        audio = r.listen(source) 

    try:
        print("Recognising ...")
        query = r.recognize_google(audio , language = 'en-in')
        print(f"user said : {query}\n" )

    except Exception as e:
        print(e)
        print("can you please repeat yourself ??")
        return "None"

    return query

speak(f"initialising System...")


if __name__ == "__main__":
    clear = lambda : os.system('cls')
    clear()
    WishMe()
    user()
    
    while True: 
        query = takeCommand().lower()
        '''All the commands said by user will be 
		   stored here in 'query' and will be
		   converted to lower case for easily 
		   recognition of command'''

        if ' wikipedia' in query:
            speak("searching wikipedia....")
            query = query.replace('wikipedia', "")
            results = wikipedia.summary(query , sentences =5)
            speak("According to wikipedia")
            speak(results)
            print(results)

        elif 'open youtube' in query:
            speak("here we go...")
            webbrowser.open("http://youtube.com")

        elif 'open google' in query:
            speak("here we go...")
            webbrowser.open("http ://www.google.com")

        elif 'open python site' in query:
            speak("here we go...")
            webbrowser.open("http://www.python.org")

        elif 'open wordpress' in query:
            speak("here we go...")
            webbrowser.open("http : //www.wordpress.com")

        elif 'open geekforgeeks' in query:
            speak("here we go...")
            webbrowser.open("http : //www.geeksforgeeks.com")

        elif 'play songs' in query or 'play music' in query or ' play a song for me' in query:
            music_dir = 'D:\Project SyberZ\Songs'
            songs = os.listdir(music_dir)
            print(songs)
            random = os.startfile(os.path.join(music_dir , songs[0]))

        elif "what the time " in query or 'time' in query:
            strTime =datetime.datetime.now().strftime("%H : %M :%S")
            speak(f"{usern} ! the time is {strTime}")


        elif 'how are you' in query or ' how are you doing' in query or  'Are you well ' in query:
            speak (" I am fine as always, Thank you for asking")

        elif "change your name" in query:
            speak(" what name you wanna like to give")
            asn = takeCommand()
            speak("thanks for your consideration !")
            speak("whats your name")
            speak(asn);
            print(asn);
            

        elif "exit" in query or "bye" in query or 'close' in query or'good bye' in query:
            speak("thanks for being humble to me ! Good Day Sir")
            exit()

        elif "joke" in query:
            speak(pyjokes.get_joke())

        elif 'news' in statement:
            news = webbrowser.open('https: //timesofindia.indiatimes.com//home//headlines')
            speak(' today headlines are :')
            time.sleep(6)

        elif "write a note " in query:
            speak("what should i write")
            note =takeCommand()
            file= open("Veronica.txt" ,'w')
            speak("Should I include the date too ?")
            inc = takeCommand()
            if "yes " in inc or "sure" in inc:
                strTime = datetime.datetime.now()
                file.write(strTime)
                file.write(" :--")
                file.write(note)

            else:
                file.write(note) 

        elif "restart the system " in query:
            speak("Are you sure ?")
            if 'yes' in query:
                subprocess.Call({"shutdown", "/r"})

        elif("open VsCode") in query:
            openfile = r"C:\\Users\\Asus\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(openfile)
        
        elif 'search' in query:
            speak("what do you want to search for?")
            searchwhat = takeCommand()
            url ="https://google.com/search?q=" + searchwhat
            webbrowser.get().open(url)
            speak("here is what i found for" +searchwhat)

        elif 'hibernate' in query or "sleep " in query:
            speak ("hibernating...")
            subprocess.Call("shutdown / h")

        elif "log off" in query:
            speak("Are you sure ?")
            takeCommand()
            if 'yes' in query:
                time.sleep(5)
                subprocess.call(["shutdown", "/l"])
            

        elif "nice" in query:
            speak("my pleasure Sir ! anything for you !!")

        elif "what i am to you " in query:
            speak(" My Master and my luv !")
        
        elif" who made you ?" in query or " who created you ?" in query:
            speak("its a top secret ! hahaha")

        
        elif "where is" in query:
            query = query.replace("where is", "")
            location = query
            speak("getting the location")
            speak(location)
            webbrowser.open("https://www.google.nl / maps / place/" + location + "")
        

        
       
