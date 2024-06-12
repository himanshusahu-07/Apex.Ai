import pyttsx3
import speech_recognition
import requests
from bs4 import BeautifulSoup
import datetime
import pyautogui
import Keyboard
import os
import speech_recognition
engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id)
rate = engine.setProperty("rate",170)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def takeCommand():
    r = speech_recognition.Recognizer()
    with speech_recognition.Microphone() as source:
        print("Listening.....")
        r.pause_threshold = 1
        r.energy_threshold = 300
        audio = r.listen(source,0,4)

    try:
        print("Understanding....")
        query  = r.recognize_google(audio,language='en-in')
        print(f"You Said: {query}\n")
    except Exception as e:
        print("Say that again")
        return "None"
    return query


if __name__ == "__main__":
    while True:
        query = takeCommand().lower()
        if "wake up" in query:
            from Greetme import greetMe
            greetMe()

            while True:
                query = takeCommand().lower()
                if "go to sleep" in query:
                    speak("Ok sir , You can me call anytime")
                    break

                elif "news " in query :
                    from  news import latestnews
                    latestnews()

                elif "hello" in query:
                    speak("Hello sir, how are you ?")

                elif "i am fine" in query:
                    speak("that's great, sir")

                elif "how are you" in query:
                    speak("Perfect, sir")

                elif "thank you" in query:
                    speak("you are welcome, sir")

                elif "play a game" in query:
                    from game import game_play
                    game_play()

                elif "pause" in query:
                    pyautogui.press("k")
                    speak("video paused")

                elif "play" in query:
                    pyautogui.press("k")
                    speak("video played")

                elif "mute" in query:
                    pyautogui.press("m")
                    speak("video muted")

                elif "volume up" in query:
                    from Keyboard import volumeup
                    speak("Turning volume up,sir")
                    volumeup()

                elif "volume down" in query:
                    from Keyboard import volumedown
                    speak("Turning volume down, sir")
                    volumedown()


                elif "open" in query:
                    from Dictapp import openappweb
                    openappweb(query)
                    
                elif "close" in query:

                    from Dictapp import closeappweb
                    closeappweb(query)

                elif "google" in query:
                    from SearchNow import searchGoogle
                    searchGoogle(query)


                elif " youtube" in query:
                    from SearchNow import searchYoutube
                    searchYoutube(query)

                elif "wikipedia" in query:
                    from SearchNow import searchWikipedia
                    searchWikipedia(query)

                elif "whatsapp" in query:
                    from Whatsapp import sendMessage
                    sendMessage()

                elif "calculate" in query:
                    from Calculatenumbers import wolframalpha
                    from Calculatenumbers import Calc
                    query = query.replace("calculate","")
                    query =query.replace("Apex" ,"")
                    Calc(query)
               

                elif "temperature" in query:
                    search = "temperature in Indore"
                    url = f"https://www.google.com/search?q={search}"
                    r  = requests.get(url)
                    data = BeautifulSoup(r.text,"html.parser")
                    temp = data.find("div", class_ = "BNeawe").text
                    speak(f"current{search} is {temp}")
                    print(temp)
                    

                elif "weather" in query:
                    search = "temperature in Indore"
                    url = f"https://www.google.com/search?q={search}"
                    r  = requests.get(url)
                    data = BeautifulSoup(r.text,"html.parser")
                    whe = data.find("div", class_ = "BNeawe").text
                    speak(f"current{search} is {whe}")
                    print(whe)


                elif "the time" in query:
                    strTime = datetime.datetime.now().strftime("%H:%M")
                    speak(f"Sir, the time is {strTime}")


                elif "remember that" in query:
                    rememberMessage = query.replace("remember that","")
                    rememberMessage = query.replace("jarvis","")
                    speak("You told me to remember that"+rememberMessage)
                    remember = open("Remember.txt","a")
                    remember.write(rememberMessage)
                    remember.close()


                elif "what do you remember" in query:
                    remember = open("Remember.txt","r")
                    speak("You told me to remember that" + remember.read())



                elif "shutdown the system" in query:
                    speak("Are You sure you want to shutdown")
                    shutdown = input("Do you wish to shutdown your computer? (yes/no)")
                    if shutdown == "yes":
                        os.system("shutdown /s /t 1")

                    elif shutdown == "no":
                        break


                # elif "finally sleep" or "sleep" in query:
                #   speak("Going to sleep,sir")
                #   exit()


