import pyttsx3
import speech_recognition as sr
import requests
from bs4 import BeautifulSoup
import datetime
import pyautogui
import os
import keyboard

# Initialize the speech engine
engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id)
engine.setProperty("rate", 170)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def take_command():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.pause_threshold = 1
        recognizer.energy_threshold = 300
        audio = recognizer.listen(source, 0, 4)

    try:
        print("Understanding...")
        query = recognizer.recognize_google(audio, language='en-in')
        print(f"You said: {query}\n")
    except Exception as e:
        print("Could not understand. Please say that again.")
        return "None"
    return query.lower()


if __name__ == "__main__":
    while True:
        query = take_command()

        if "wake up" in query:
            from Greetme import greetMe
            greetMe()

            while True:
                query = take_command()

                if "go to sleep" in query:
                    speak("Okay sir, you can call me anytime.")
                    break

                elif "news" in query:
                    from news import latestnews
                    latestnews()

                elif "hello" in query:
                    speak("Hello sir, how are you?")

                elif "i am fine" in query:
                    speak("That's great, sir.")

                elif "how are you" in query:
                    speak("Perfect, sir.")

                elif "thank you" in query:
                    speak("You're welcome, sir.")

                elif "play a game" in query:
                    from game import game_play
                    game_play()

                elif "pause" in query:
                    pyautogui.press("k")
                    speak("Video paused.")

                elif "play" in query:
                    pyautogui.press("k")
                    speak("Video played.")

                elif "mute" in query:
                    pyautogui.press("m")
                    speak("Video muted.")

                elif "volume up" in query:
                    speak("Turning volume up, sir.")
                    volumeup()

                elif "volume down" in query:
                    speak("Turning volume down, sir.")
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

                elif "youtube" in query:
                    from SearchNow import searchYoutube
                    searchYoutube(query)

                elif "wikipedia" in query:
                    from SearchNow import searchWikipedia
                    searchWikipedia(query)

                elif "whatsapp" in query:
                    from Whatsapp import sendMessage
                    sendMessage()

                elif "calculate" in query:
                    from Calculatenumbers import Calc
                    query = query.replace("calculate", "").replace("Apex", "")
                    Calc(query)

                elif "temperature" in query:
                    search = "temperature in Indore"
                    url = f"https://www.google.com/search?q={search}"
                    response = requests.get(url)
                    data = BeautifulSoup(response.text, "html.parser")
                    temp = data.find("div", class_="BNeawe").text
                    speak(f"Current {search} is {temp}.")
                    print(temp)

                elif "weather" in query:
                    search = "temperature in Indore"
                    url = f"https://www.google.com/search?q={search}"
                    response = requests.get(url)
                    data = BeautifulSoup(response.text, "html.parser")
                    weather = data.find("div", class_="BNeawe").text
                    speak(f"Current {search} is {weather}.")
                    print(weather)

                elif "the time" in query:
                    current_time = datetime.datetime.now().strftime("%H:%M")
                    speak(f"Sir, the time is {current_time}.")

                elif "remember that" in query:
                    remember_message = query.replace(
                        "remember that", "").replace("jarvis", "")
                    speak("You told me to remember that " + remember_message)
                    with open("Remember.txt", "a") as remember_file:
                        remember_file.write(remember_message + "\n")

                elif "what do you remember" in query:
                    with open("Remember.txt", "r") as remember_file:
                        remember_data = remember_file.read()
                    speak("You told me to remember that " + remember_data)

                elif "shutdown the system" in query:
                    speak("Are you sure you want to shutdown?")
                    shutdown = input(
                        "Do you wish to shutdown your computer? (yes/no): ").strip().lower()
                    if shutdown == "yes":
                        os.system("shutdown /s /t 1")
                    elif shutdown == "no":
                        break
