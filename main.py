import pyttsx3
import speech_recognition as sr
import os
import pyjokes
import keyboard
import webbrowser
import openai
from config import apikey
import datetime
import random
import numpy as np

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
print(voices)
engine.setProperty('voices', voices[0].id)
chatStr = ""
# https://youtu.be/Z3ZAJoi4x6Q
def chat(query):
    global chatStr
    openai.api_key = apikey
    chatStr += f"Sir: {query}\n Jarvis: "
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt= chatStr,
        temperature=0.7,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    # todo: Wrap this inside of a  try catch block
    say(response["choices"][0]["text"])
    print(response["choices"][0]["text"])
    chatStr += f"{response['choices'][0]['text']}\n"
    return response["choices"][0]["text"]


def ai(prompt):
    openai.api_key = apikey
    text = f"OpenAI response for Prompt: {prompt} \n *************************\n\n"

    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=prompt,
        temperature=0.7,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    # todo: Wrap this inside of a  try catch block
    # print(response["choices"][0]["text"])
    text += response["choices"][0]["text"]
    if not os.path.exists("Openai"):
        os.mkdir("Openai")

    # with open(f"Openai/prompt- {random.randint(1, 2343434356)}", "w") as f:
    with open(f"Openai/{query}.txt", "w") as f:
        f.write(text)

    say(response["choices"][0]["text"])

def say(audio):
   #audio = "beep   " + audio
   engine.say(audio)
   engine.runAndWait()

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        # r.pause_threshold =  0.6
        audio = r.listen(source)
        try:
            print("Recognizing...")
            query = r.recognize_google(audio, language="en-in")
            print(f"User said: {query}")
            return query
        except Exception as e:
            return "Some Error Occurred. Sorry from Jarvis"

if __name__ == '__main__':
    print('Welcome to Jarvis A.I')
    say("Power Initiating")
    say("What can I Do for you sir ?")
    while True:
        print("Listening...")
        query = takeCommand()
        # todo: Add more sites
        sites = [["youtube", "https://www.youtube.com"], ["wikipedia", "https://www.wikipedia.com"], ["google", "https://www.google.com"],]
        for site in sites:
            if f"Open {site[0]}".lower() in query.lower():
                say(f"Opening {site[0]} sir...")
                webbrowser.open(site[1])
        # todo: Add a feature to play a specific song
        if "how are you" in query:
            say("just fine sir! Always there to help you!")
        elif "open music" in query:
            musicPath = "J:/Storage_Vent/Personal Module/Music/Songs of Spotify/1_Bones.mp3"
            os.system(f"open {musicPath}")
        elif 'joke' in query:
            joke = pyjokes.get_joke()
            say("heres a Joke for you sir")
            say(joke)
        elif 'pause' in query:
            say('video Paused sir')
            keyboard.press('space bar')
            a = False
        elif 'play' in query:
            say("playing the video sir")
            keyboard.press('space bar')
            a = False
        elif 'mute' in query:
            say("Video  Muted Sir")
            keyboard.press('m')
            a = False
        elif 'unmute' in query:
            say('ok sir, video unmuted')
            keyboard.press('m')
            a = False
        elif 'skip' in query:
            keyboard.press('l')
            a = False
        elif 'back' in query:
            keyboard.press('j')
            a = False
        elif 'full screen' in query:
            keyboard.press("alt")
            keyboard.press("enter")
            keyboard.release("alt")
            keyboard.release("enter")
            a = False
        elif 'restart' in query:
            keyboard.press('0')
            a = False
        elif query.startswith("close it"):
            say("Closing application")
            keyboard.press("alt")
            keyboard.press("f4")
            keyboard.release("alt")
            keyboard.release("f4")
        elif "the time" in query:
            musicPath = "J:/Storage_Vent/Personal Module/Music/Songs of Spotify/1_Bones.mp3"
            hour = datetime.datetime.now().strftime("%H")
            min = datetime.datetime.now().strftime("%M")
            say(f"Sir. the time is {hour} and {min} minutes")


        elif "open discord".lower() in query.lower():
            os.system(f"open /Applications/Discord.app")

        elif "tell me".lower() in query.lower():
            query = query.replace("tell me", "")
            print("query")
            ai(prompt=query)

        elif "Jarvis Quit".lower() in query.lower():
            exit()

        elif "reset chat".lower() in query.lower():
            chatStr = ""

        else:
            chat(query)





        # say(query)