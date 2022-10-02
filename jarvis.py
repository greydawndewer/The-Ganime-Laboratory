import pyttsx3
import datetime
from playsound import playsound
import pyautogui
import pyperclip
import webbrowser
from notifypy import Notify
import speech_recognition as sr
from requests.adapters import HTTPAdapter
#'''from requests.packages.urllib3.util.retry import Retry'''
import wikipedia
from PyDictionary import PyDictionary as dict
import threading
import winsound
from requests import get
from selenium.webdriver.chrome.options import Options
import keyboard
import googletrans
from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd
from requests_html import HTML
from requests_html import HTMLSession
import urllib
import webbrowser
import json
import requests
import pyjokes
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from mutagen.mp3 import MP3
from time import sleep
import os
import pygame
from pygame import mixer
try:
    from googlesearch import search
except ImportError:
    print("No module named 'google' found")
import subprocess
# noinspection PyUnboundLocalVariable
from pynput.keyboard import Key, Controller
import pywhatkit
import fbchat
from getpass import getpass

gt = googletrans.Translator

SCOPES = ['https://www.googleapis.com/auth/calendar.readonly']
MONTHS = ["january", "february", "march", "april", "may", "june","july", "august", "september","october","november", "december"]
DAYS = ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"]
DAY_EXTENTIONS = ["rd", "th", "st", "nd"]

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
print(voices)
engine.setProperty('voices', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning Sir!")
    elif hour >= 12 and hour < 18:
        speak("Good Afternoon Sir!")
    else:
        speak("Good Evening Sir!")
    speak("Jarvis is Online!")
    speak("How may I assist You?")


def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source, 0, 2)
    try:
        print("Recognising...")
        query = r.recognize_google(audio, language='en-in')
        speak(f"hmm")
        print(f"You Said: {query}")
    except BaseException as e:
        print("Sir Speak Again!")
        speak("You may Speak Again Sir!")
        return "None"
    return query


def get_date(text):
    text = text.lower()
    today = datetime.date.today()

    if text.count("today") > 0:
        return today

    day = -1
    day_of_week = -1
    month = -1
    year = today.year

    for word in text.split():
        if word in MONTHS:
            month = MONTHS.index(word) + 1
        elif word in DAYS:
            day_of_week = DAYS.index(word)
        elif word.isdigit():
            day = int(word)
        else:
            for ext in DAY_EXTENTIONS:
                found = word.find(ext)
                if found > 0:
                    try:
                        day = int(word[:found])
                    except:
                        pass

        # THE NEW PART STARTS HERE
    if month < today.month and month != -1:
        year = year + 1

        # This is slighlty different from the video but the correct version
    if month == -1 and day != -1:  # if we didn't find a month, but we have a day
        if day < today.day:
            month = today.month + 1
        else:
            month = today.month

        # if we only found a dta of the week
    if month == -1 and day == -1 and day_of_week != -1:
        current_day_of_week = today.weekday()
        dif = day_of_week - current_day_of_week

        if dif < 0:
            dif += 7
            if text.count("next") >= 1:
                dif += 7

        return today + datetime.timedelta(dif)

    if day != -1:  # FIXED FROM VIDEO
        return datetime.date(month=month, day=day, year=year)

def get_source(url):

    try:
        session = HTMLSession()
        response = session.get(url)
        return response

    except requests.exceptions.RequestException as e:
        print(e)

def get_audio():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)
        said = ""

        try:
            said = r.recognize_google(audio)
        except Exception as e:
            print("Exception: " + str(e))

    return said.lower()




a = True
if __name__ == '__main__':
    wishMe()
    while a == True:
        tnow = datetime.datetime.now()
        d = datetime.datetime(tnow.year, tnow.month, tnow.day, 19, 5, 00)
        d1 = datetime.datetime(tnow.year, tnow.month, tnow.day, 20, 5, 00)
        if tnow >= d and tnow <= d1:
            speak("Sir, You Should Study Now! Its Past 7 PM")
            query = takecommand().lower()
            if 'ok thanks' in query:
                speak("No Problem Sir, Happy Study")
                speak("going in standby mode")
                a = False
            while not 'ok thanks' in query:
                speak("Please Sir")
                query = takecommand().lower()
                if 'ok thanks' in query:
                    speak("No Problem Sir, Happy Study")
                    speak("going in standby mode")
                    a = False
        if a == True:
            query = takecommand().lower()
            if 'wikipedia' in query:
                speak("Searching Wikipedia...")
                query = query.replace('wikipedia', "")
                results = wikipedia.summary(query, sentences=2)
                speak("According To Wikipedia")
                print(results)
                speak(results)
                a = False
            elif 'hello jarvis' in query:
                speak("Hello Sir, I am Great How was Your Day")
                query = takecommand().lower()
                speak("Awsome Sir! You Shall Do Your Projects Also!")
                a = False
            elif 'send facebook message' in query:
                speak("Sir for sending a Message, See the Console and Type the Info Please!")
                username = input("Username: ")
                client = fbchat.Client(username, getpass())
                no_of_friends = int(input("Number of friends: "))
                for i in range(no_of_friends):
                    name = input("Name: ")
                    friends = client.searchForUsers(name)  # return a list of names
                    friend = friends[0]
                    msg = input("Message: ")
                    sent = client.sendMessage(msg, thread_id=friend.uid)
                    if sent:
                        speak("Message sent succesfully Sir")
                        print("Message sent successfully!")
                a = False
            elif 'open youtube and search' in query:
                speak("Openning Youtube!")
                query = query.replace('open youtube and search', "")
                if 'jarvis' in query:
                    query = query.replace('jarvis', "")
                webbrowser.open(f'https://youtube.com/results?search_query={query}')
                a = False
            elif 'my location' in query:
                speak("Heres Your Location Sir ")
                webbrowser.open("https://www.google.com/maps/place/Swarnjyoti+Colony,+Bistupur,+Jamshedpur,+Jharkhand+831005"
                         + "/@22.7940679,86.1709209,17z/data=!4m5!3m4!1s0x39f5e49e7b967d41:0x893282463d39ccc7!8m2!3d22."
                          + "7940679!4d86.1731096")
                a = False
            elif 'close Google' in query:
                speak("Closing Google Sir...")
                os.system("TASKKILL /F /im chrome.exe")
                a = False
            elif 'open website' in query:
                query = query.replace('open website', "")
                query = query.replace('jarvis', "")
                query = query.replace(' ', "")
                webbrowser.open(f'https://www.{query}.com')
                a = False
            elif 'open settings' in query:
                speak("Opening Settings...")
                webbrowser.open('chrome://settings/?search=passwords')
                a = False
            elif 'send long message' in query:
                query = query.replace('send message', "")
                query = query.replace('jarvis', "")
                speak("Tell Me The Name of The Person Sir")
                query7 = str(takecommand().lower())
                print(query7)
                if 'papa' in query7:
                    speak("Tell me The Message")
                    query0 = takecommand().lower()
                    while 'none' in query0:
                        speak("Tell me The Message")
                        query0 = takecommand().lower()
                    speak("Tell me the current Hour Sir")
                    query1 = takecommand()
                    if 'Tu' in query1:
                        query1 = 2
                    speak("Now Tell me the current Minute Sir")
                    query2 = int(takecommand())
                    pywhatkit.sendwhatmsg("+919934360377", query0, query1, query2, 10)
                    speak("Sending Whatsapp Message To Papa Sir")
                if 'didi' in query7 or 'pragya' in query7:
                    speak("Tell me The Message")
                    query08 = takecommand().lower()
                    while 'none' in query08:
                        speak("Tell me The Message")
                        query08 = str(takecommand().lower())
                    speak("Tell me the current Hour Sir")
                    query1 = takecommand()
                    if 'Tu' in query1:
                        query1 = 2
                    speak("Now Tell me the current Minute Sir")
                    query2 = int(takecommand())
                    pywhatkit.sendwhatmsg("+917091500107", query08, query1, query2, 10)
                while not 'papa' in query7 or not 'pragya' in query7 or not 'didi' in query7:
                    speak("Tell Me The Name of The Person Sir")
                    query7 = str(takecommand().lower())
                    if 'papa' in query7:
                        speak("Tell me The Message")
                        query0 = takecommand().lower()
                        while 'none' in query0:
                            speak("Tell me The Message")
                            query0 = takecommand().lower()
                        speak("Tell me the current Hour Sir")
                        query1 = takecommand()
                        if 'Tu' in query1:
                            query1 = 2
                        speak("Now Tell me the current Minute Sir")
                        query2 = int(takecommand())
                        pywhatkit.sendwhatmsg("+919934360377", query0, query1, query2, 10)
                        speak("Sending Whatsapp Message To Papa Sir")
                        a = False
                    if 'didi' in query7 or 'pragya' in query7:
                        speak("Tell me The Message")
                        query08 = takecommand().lower()
                        while 'none' in query08:
                            speak("Tell me The Message")
                            query08 = str(takecommand().lower())
                        speak("Tell me the current Hour Sir")
                        query1 = takecommand()
                        if 'Tu' in query1:
                            query1 = 2
                        speak("Now Tell me the current Minute Sir")
                        query2 = int(takecommand())
                        pywhatkit.sendwhatmsg("+917091500107", query08, query1, query2, 10)
                a = False
            elif 'send a message' in query:
                query.replace("send whatsapp message", "")
                query.replace("jarvis", "")
                speak("Type the nummber in the conolse sir")
                num = input("Type Number:")
                m_num = "+91" + num
                speak("Type your message sir")
                msg = input("/nType Message: ")
                open_chat = 'https://web.whatsapp.com/send?photo=' + m_num + '&text=' + msg
                webbrowser.open(open_chat)
                sleep(120)
                keyboard.press('enter')
                a = False
            elif 'open my school notes' in query:
                speak("Opening Your school Notes Sir...")
                os.startfile("C:\\Users\\PRAGYA\\Desktop\\myschool_notes.txt")
                a = False
            elif 'open calculator' in query:
                speak("Calculator is Running sir")
                def instructions():
                    speak("say the operation in first answer and then say the numbers on which the operation should be "
                          "done")
                    speak("say end jarvis to exit calculator")
                    speak("Say Addition, subtractraction Mulltiplication or division to choose a operation sir")
                    speak("say 2 or more numbers to perform the operaton... A small note that you can calculate with 2 "
                          "or more operatores")
                    speak("say and after each number")
                speak("Say the operation sir")
                opera = takecommand().lower()
                speak("say the numbers sir")
                nums = takecommand().lower()
                nums = nums.split()
                print(nums)
                sum = 0
                base = 0
                diff = 0
                product = 0
                questiont = 0
                obs = []
                if "and" in nums:
                    for l in nums:
                        if l == " ":
                            l = l.replace(" ", "")
                        if l == "and":
                            print(l)
                            l = ""
                        obs += l
                if "addition" in opera:
                    print(obs)
                    for k in obs:
                        print(k)
                        k = int(k)
                        sum += k
                    speak(f"the sum of {obs} is {sum}")
                elif "subtarction" in opera:
                    base = obs[0]
                    difference += base - obs[1]
                    for k in obs:
                        k = int(k)
                        difference -= k
                    speak(f"the difference of {obs} is {difference}")
                elif "multiplication" in opera:
                    prodcut += obs[0]
                    for k in obs:
                        k = int(k)
                        product *= k
                    speak(f"the product of {obs} is {product}")
                elif 'division' in query:
                    questiont += obs[0] / obs[1]
                    speak(f"the difference of {obs} is {difference}")
                speak("Sir, Would You like to do?")
                speak('A - Calculate more numbers')
                speak("B - Tell me the instructions")
                speak("Exit calculatore")
                speak("say A B or C to choose")
                option = takecommand().lower()
                while option != "exit calculator":
                    if option == "a":
                        speak("Say the operation sir")
                        opera = takecommand().lower()
                        speak("say the numbers sir")
                        nums = takecommand().lower()
                        nums = nums.split()
                        sum = 0
                        base = 0
                        diff = 0
                        product = 0
                        questiont = 0
                        obs = []
                        if "and" in nums:
                            for l in nums:
                                if l == "and":
                                    l = ""
                                    l = int(l)
                                    obs += l
                        if "addition" in opera:
                            for k in obs:
                                sum += k
                            speak(f"the sum of {obs} is {sum}")
                        elif "subtarction" in opera:
                            base = obs[0]
                            difference += base - obs[1]
                            for k in obs:
                                difference -= k
                            speak(f"the difference of {obs} is {difference}")
                        elif "multiplication" in opera:
                            prodcut += obs[0]
                            for k in obs:
                                product *= k
                            speak(f"the product of {obs} is {product}")
                        elif 'division' in query:
                            questiont += obs[0] / obs[1]
                            speak(f"the difference of {obs} is {difference}")
                        speak("Anything else sir? if not say exit calculator")
                        option = takeecommand().lower()
                    elif option == "b":
                        speak("Loading instructions sir")
                        sleep(3)
                        instructions()
                        speak("Anything else sir? if not say exit calculator")
                        option = takeecommand().lower()
                    else:
                        speak("Invalid choice, try again")
                        option = takeecommand().lower()
                else:
                    speak("Exiting Calculator sir")
                    a = False
            elif "what should i do" in query:
                weekday = datetime.datetime.now().strftime(f"%A")
                speak(f"checking about {weekday.lower()}...")
                sleep(3)
                print(weekday)
                weeeedays = ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday"]
                if weekday.lower() in weeeedays:
                   from weekdaytable import Time
                   value = Time()
                   noti1 = Notify()
                   noti1.title = "Weekday Timetable"
                   noti1.message = str(value)
                   noti1.send()
                else:
                   from sundaytable import Time as Time1
                   value1 = Time1()
                   noti2 = Notify()
                   noti2.title = "Sunday Timetable"
                   noti2.message = str(value1)
                   noti2.send()
            elif "initiate mark 2" in query:
                speak("activiting Protocol mark 2")
                speak("starting Web scraping test")
                URL = "https://www.google.com/search?q=biology&sxsrf=ALiCzsb43iDHharwPH4j3jKfTksXVKM9Wg%3A1656755074" \
                      "344" \
                      "&" \
                      "ei=ghPAYrrSFMnl4-EPgvEf&oq=bio&gs_lcp=Cgdnd3Mtd2l6EAEYADIECCMQJzIECCMQJzIFCAAQkQIyCAgAEIAEEL" \
                      "EDMgUIABCABDIFCAAQsQMyBQgAEIAEMgUIABCxAzIFCAAQsQMyCAgAEIAEELEDOgcIIxDqAhAnOgQILhAnOgQIABBDOg4" \
                      "ILhCABBCxAxDHARDRAzoICC4QgAQQsQM6CAgAELEDEIMBOgsIABCABBCxAxCDAUoECEEYAEoECEYYAFA" \
                      "AWIMKYI8naAFwAX" \
                      "gAgAHiAYgBqQSSAQUwLjIuMZgBAKABAbABCsABAQ&sclient=gws-wiz"
                page = requests.get(URL)

                soup = BeautifulSoup(page.content, "html.parser")
                print(soup)
                speak("Printed soup")
                speak("protocol ended")
            elif "tell" in query:
                print("entered")
                query = query.replace("tell me", "")
                import wikipedia as googleScrap2
                print(query)
                speak("Searching google for your search...")
                sleep(3)
                pywhatkit.search(query)
                try:
                    result = googleScrap2.summary(query, 5)
                    speak(result)
                    a = False
                except:
                    speak("No Speakable Result")
                    speak("You shall see yourself sir")
                    speak("Opening your result in chrome sir")
                    webbrowser.open(f'https://www.google.com/search?q={query}')
                a = False
            elif 'search' in query:
                speak("Searching...")
                query = query.replace('search', "")
                if 'jarvis' in query:
                    query = query.replace('jarvis', "")
                speak('Here are The Results I found:')
                webbrowser.open(f'https://www.google.com/search?q={query}')
                a = False
            elif 'open youtube' in query:
                speak("Openning Youtube!")
                query = query.replace('open youtube', "")
                webbrowser.open(f'https://youtube.com')
                a = False
            elif 'pause' in query:
                speak('video Paused sir')
                keyboard.press('space bar')
                a = False
            elif 'play' in query:
                speak("playing the video sir")
                keyboard.press('space bar')
                a = False
            elif 'mute' in query:
                speak("Video  Muted Sir")
                keyboard.press('m')
                a = False
            elif 'unmute' in query:
                speak('ok sir, video unmuted')
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
            elif "reboot yourself" in query:
                speak("rebooting")
                keyboard.press("shift")
                keyboard.press("f10")
                keyboard.release("shift")
                keyboard.release("f10")
            elif query.startswith("close it"):
                speak("Closing application")
                keyboard.press("alt")
                keyboard.press("f4")
                keyboard.release("alt")
                keyboard.release("f4")
            elif 'Close tab' in query:
                keyboard.press("ctrl")
                keyboard.press("w")
                keyboard.release("ctrl")
                keyboard.release("w")
                a = False
            elif 'Open new tab' in query:
                keyboard.press("ctrl")
                keyboard.press("t")
                keyboard.release("ctrl")
                keyboard.release("t")
                a = False
            elif 'joke' in query:
                joke = pyjokes.get_joke()
                speak("heres a Joke for you sir")
                speak(joke)
                a = False
            elif 'open google' in query:
                speak("Opening Chrome...")
                app = 'C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe'
                subprocess.Popen(app)
                a = False
            elif 'open discord' in query:
                speak("Opening Web Discord...")
                webbrowser.open(f'https://discord.com/')
                a = False
            elif 'who is my sister' in query:
                speak(
                    "Your Sister is Pragya Priyadarshini, She is 23 Years Old, She is a Bright Student and She wants to"),
                speak("be a Docter, She is Trying For it from Many years and Has Reached On a Master Level, She Likes")
                speak(
                    "Paneer and Chicken The Most and As most girls, she has Everything Fucking PINK. She Loves Biology")
                speak(
                    "She Doesnt Give a Shit About Her COOL DASHING Brother, My owner. He hopes she will play with her")
                speak("After her College Entrence. She works Very Hard for it")
                speak("And I Jarvice is pretty Sure that she will make it to be a docter,Dont be offended")
                a = False
            elif 'who is my father' in query:
                speak('Sir, Your Father is Pradip Kumar Mishra, He is 56 Years Old. He works in Goods and Services'),
                speak('Taxes (GST), a Govermental Job in Which he is a Supritendent of Tribunal Review. He likes'),
                speak(' Classic Music and He doesnt leaves a shopping store quickly. he likes sweets as he is sweet '),
                speak('and He is` the best dad I jarvis has seen ever')
                a = False
            elif 'type word' in query:
                query = query.replace('type word', "")
                query = query.replace('jarvis', "")
                query.upper()
                keyboard = Controller()
                key = f"{query}"

                keyboard.press(key)
                keyboard.release(key)
                a = False
            elif 'set alarm' in query:
                inp = '07:30:00'
                hgu = '07:30:45'
                speak("alarm set sir")
                y = True
                while True:
                    nowt = datetime.datetime.now().strftime('%H:%M:%S')
                    if inp == nowt or inp <= nowt:
                        speak("Wake Up Sir...")
                        playsound("C:\\Users\\PRAGYA\\Music\\Music\\alarm_music.mp3")
                        speak("Sir its a Important Day, You shall study now")
                        playsound("C:\\Users\\PRAGYA\\Music\\Music\\alarm_music.mp3")
                        speak("Sir its a Important Day, You shall study now")
                        playsound("C:\\Users\\PRAGYA\\Music\\Music\\alarm_music.mp3")
                        speak("Alarm Closed Sir")
                        quit()
                a = False
            elif 'check speed' in query:
                import speedtest
                speed = speedtest.Speedtest()
                downloading = speed.download()
                correctdown = int(downloading/800000)
                uploading = speed.upload()
                correctupload = int(uploading/800000)
                if 'uploading' in query:
                    speak("Checking Uploading Speed...")
                    speak(3)
                    speak(f"The Uploading Speed Of Your WiFi is {correctupload} mbps")
                elif 'downloading' in query:
                    speak("Checking Downloading Speed...")
                    speak(3)
                    speak(f"The Downloading Speed Of Your WiFi is {correctdown} mbps")
                else:
                    speak("Checking The Speed...")
                    sleep(3)
                    speak(f"The Uploading Speed Of Your WiFi is {correctupload} mbps and The Downloading Speed Of Your"
                          f" WiFi "
                          f"is {correctdown} mbps")
                a = False
            elif 'open dictionary' in query:
                speak("Opening Dicrionary For You Sir...")
                speak("Please Tell What is Your Problem...")
                b1 = takecommand().lower()
                if 'meaning' in b1:
                    b1 = b1.replace("meaning", "")
                    result = dict.meaning(b1)
                    speak(f"The Meaning of {b1} is {result}.")
                if 'antonym' in b1:
                    b1 = b1.replace("antonym", "")
                    result = dict.antonym(b1)
                    speak(f"The Antonym of {b1} is {result}.")
                if 'synonym' in b1:
                    b1.replace("synonym", "")
                    result = dict.synonym(b1)
                    speak(f"The Synonym of {b1} is {result}.")
                a = False
            elif 'leave message' in query:
                query = query.replace('leave message', "")
                query = query.replace('jarvis', "")
                while True:
                    speak(query)
                    sleep(10)
                a = False
            elif 'close Google' in query:
                speak("Closing Google Sir...")
                os.system("TASKKILL /F /im chrome.exe")
                a = False
            elif 'music' in query:
                speak("Here is the List of Music! You shall Look in the Console for Text Sir!")
                query = query.replace('play music', '')
                music_dir = 'C:\\Users\\PRAGYA\\Music\\Music'
                songs = os.listdir(music_dir)
                print("Current Songs:")
                print(songs)
                speak("Tell Which Song to Play By Number")
                print("Tell Which Song to Play By Number")
                query1 = takecommand().lower()
                if 'tu' in query1:
                    query1 = query1.replace('tu', '2')
                query1 = int(query1)
                query1 -= 1
                y = songs[query1]
                a = False
                os.startfile(os.path.join(music_dir, songs[query1]))
                print("Currently Playing: " + songs[0])
            elif "remember that" in query:
                rmbMsg = query.replace("remember that", "")
                if 'jarvis' in query:
                  rmbMsg = rmbMsg.replace("jarvis", "")
                speak("Ok sir I will remember that, " + rmbMsg)
                remember = open("reminder.txt", "w")
                remember.write(rmbMsg)
                remember.close()
                a = False
            elif "repeat after me" in query:
                speak("Just say the word to repeat sir and say stop jarvis when to stop")
                rep = takecommand().lower()
                while rep != "stop jarvis":
                    speak(rep)
                    rep = takecommand().lower()
                speak("ok sir")
                a = False
            elif "where am i" in query:
                speak("Searching Satelites...")
                my_add = get("https://api.ipify.org").text
                url = "https://get.geojs.io/v1/ip/geo/" + my_add + ".json"
                geo_q = requests.get(url)
                geo_d = geo_q.json()
                state = geo_d['city']
                country = geo_d['country']
                speak(f"Sir, You are in {state}, {country}")
            elif "what do you remember" in query:
                with open('reminder.txt') as f:
                    remember = f.readlines()
                    speak("You told me to remember that " + remember[0])
                    a = False
            elif "temperature" in query:
                query = query.replace("temperature in", "")
                if 'what is the' in query:
                    query = query.replace("what is the", "")
                if "jarvis" in query:
                    query = query.replace("jarvis", "")
                if 'Jarvis' in query:
                    query = query.replace("Jarvis", "")

                api_key = "03fb7ccae2cc1facf6714847a6370b26"

                # base_url variable to store url
                base_url = "http://api.openweathermap.org/data/2.5/weather?"

                # Give city name
                city_name = query
                print(f"City: {city_name}")

                # complete_url variable to store
                # complete url address
                complete_url = base_url + "appid=" + api_key + "&q=" + city_name

                # get method of requests module
                # return response object
                response = requests.get(complete_url)

                # json method of response object
                # convert json format data into
                # python format data

                x = response.json()


                # Now x contains list of nested dictionaries
                # Check the value of "cod" key is equal to
                # "404", means city is found otherwise,
                # city is not found

                if x["cod"] != "404":

                    # store the value of "main"
                    # key in variable y
                    y = x["main"]

                    # store the value corresponding
                    # to the "temp" key of y
                    current_temperature = y["temp"]
                    temp_in_c = current_temperature - 273.15
                    print(f"Temperature: {int(temp_in_c)} degree C")
                    # store the value corresponding
                    # to the "pressure" key of y
                    current_pressure = y["pressure"]
                    print(f"Air Pressure: {current_pressure} hactopascal")

                    # store the value corresponding
                    # to the "humidity" key of y
                    current_humidity = y["humidity"]
                    print(f"Humidity: {current_humidity}%")

                    # store the value of "weather"
                    # key in variable z
                    z = x["weather"]

                    # store the value corresponding
                    # to the "description" key at
                    # the 0th index of z
                    weather_description = z[0]["description"]
                    speak(f"Sir, Todays Temperature in {query} is {int(temp_in_c)} degree celsius, The Pressure is"
                          f" {current_pressure} hactopascal, and the Humidity is {current_humidity}%, And"
                          f" Its {weather_description} Sir, Thats it Sir")
                a = False
            elif 'reminders' in query:
                speak("Sir You had to")
                speak("1 Do your Physics Copy Work")
                speak('2 your Bio work')
                speak("3 Your Maths Project and Practise")
                speak('4 Stick project pics')
                speak("5 Do the Sign and Symbols")
                speak("6 Learn English Language Speech")
                a = False
            elif "what is today's news on" in query:
                topic = query.replace("what is today's news on ", "")
                speak(f"Checking Latest Hot News for {topic}")
                sleep(5)
                from gnewsclient import gnewsclient

                client = gnewsclient.NewsClient(language='english',
                                                location='india',
                                                topic=topic.lower(),
                                                max_results=5)

                news_list = client.get_news()

                for item in news_list:
                    print("Title : ", item['title'])
                    speak(f"{item['title']}")
                    print("")
                speak("sir do you want more news?")
                yn = takecommand().lower()
                while "ok" in yn or "on" in yn or "yes" in yn:
                    if "ok" in yn:
                        speak("ok sir, checking more news")
                        sleep(5)
                        client = gnewsclient.NewsClient(language='english',
                                                        location='india',
                                                        topic=topic.lower(),
                                                        max_results=5)

                        news_list = client.get_news()

                        for item in news_list:
                            print("Title : ", item['title'])
                            speak(f"{item['title']}")
                            print("")
                        speak("sir do you want more news?")
                        yn = takecommand().lower()
                    elif "yes but on" in yn:
                        yn = yn.replace("yes but on", "")
                        speak("ok sir, checking more news for new topic")
                        sleep(5)
                        client2 = gnewsclient.NewsClient(language='english',
                                                         location='india',
                                                         topic= yn.lower(),
                                                         max_results=5)

                        news_list = client2.get_news()

                        for item in news_list:
                            print("Title : ", item['title'])
                            speak(f"{item['title']}")
                            print("")
                        speak("sir do you want more news?")
                        yn = takecommand().lower()
                    else:
                        speak("ok sir, thanks for eharing the news!")
                        a = False
            elif 'good morning' in query:
                strtime = datetime.datetime.now().strftime(f"%H")
                hour = int(datetime.datetime.now().hour)
                a = False
                speak("Good Morning Sir, Today is a Wonder Full Day and Its {hour}`o clock Sir, You shall Study")
            elif 'tell my remaining projects' in query:
                speak(
                    "Sir, You have 4 Projects Remaing, of Maths, Physics, Chemistry and Biology, You shall Do CHemistry")
                speak("First Sir! You have to Write Table 1 of 30 Elements and About Thier Element Name and Symbol and")
                speak("Thier Atomic Number")
                speak("and Thier Mass Number and Number of Electrons, Protons and Nutrons Also Sir")
                speak("In Table 2 You have to Differntiate the elements  all 30 in Metals, Non metals and Metaloids Sr")
                speak(
                    "In Table 3 ou have To Write Formulas of 50 Compunds given in Page Number 42 in Chemistry Main Book")
                speak("and also in Page number 21 of Chemical Communication Book, You have to write the formula with")
                speak("cris-cross method like in the rough copy. Then, You have write the Elctron Confrigation of All")
                speak(" 30 Elements like how manyy electron in K shell, L shell, M shell and N Shell! Thats It Sir")
                sleep(3)
                speak("Do you want me to Repeat Sir?")
                query = takecommand().lower()
                if 'yes' in query:
                    while 'yes' in query:
                        speak(
                            "Sir, You have 4 Projects Remaing, of Maths, Physics, Chemistry and Biology, You shall Do CHemistry")
                        speak(
                            "First Sir! You have to Write Table 1 of 30 Elements and About Thier Element Name and Symbol and")
                        speak("Thier Atomic Number")
                        speak("and Thier Mass Number and Number of Electrons, Protons and Nutrons Also Sir")
                        speak(
                            "In Table 2 You have to Differntiate the elements  all 30 in Metals, Non metals and Metaloids Sir")
                        speak(
                            "In Table 3 you have To Write Formulas of 50 Compunds given in Page Number 42 in Chemistry Main Book")
                        speak(
                            "and also in Page number 21 of Chemical Communication Book, You have to write the formula with")
                        speak(
                            "cris-cross method like in the rough copy. Then, Table 4 is You have write the Elctron Confrigation of All")
                        speak(
                            " 30 Elements like how manyy electron in K shell, L shell, M shell and N Shell! Thats It Sir")
                        speak("do you want me to repeat again sir?")
                        query = takecommand().lower()
                if 'no' in query:
                    speak("ok sir")
                    speak("You Shall Study Now Sir, Going in Stand By Mode")
                    a = False
                a = False
            elif "the time" in query:
                strtime = datetime.datetime.now().strftime(f"%H:%M")
                hour = int(datetime.datetime.now().hour)
                if hour >= 0 and hour < 12:
                    speak(f"Sir, the time is {strtime} AM , Good Morning!")
                elif hour >= 12 and hour < 18:
                    speak(f"Sir, the time is {strtime} PM , Good AFternoon!")
                elif hour >= 18 and hour < 21:
                    speak(f"Sir, the time is {strtime} PM , Good Evening!")
                else:
                    speak(f"Sir, the time is {strtime} PM , Good Night!")
                print(f"Sir, the time is {strtime}")
                a = False
            elif 'open classroom' in query:
                speak("Opening Google Classroom Sir...")
                webbrowser.open('https://classroom.google.com/u/0/h')
                a = False
            elif "what is today's date" in query:
                strdate = datetime.datetime.now().strftime(f"%d %B")
                weekday = datetime.datetime.now().strftime(f"%A")
                speak(f"Sir todays date is {strdate} and its {weekday}")
            elif 'thank you' in query:
                speak("No Probem Sir!")
                a = False
            elif 'go in standby mode' in query or 'go to sleep' in query:
                speak("Going in Stand By Mode Sir, Please Say Jarvis For Returning Me Back To Active Mode")
                a = False
            elif 'open YouTube history' in query:
                speak("Opening Your Youtube History Sir")
                webbrowser.open('https://www.youtube.com/feed/history')
                a = False
            elif 'open WhatsApp' in query:
                speak("Opening Whatsapp Sir...")
                webbrowser.open('https://web.whatsapp.com/')
                speak("You shall Check the messages sir")
                a = False
            elif "note in notepad" in query:
                 speak("Sir, Just tell me what to write")
                 writes = takecommand().lower()
                 speak("sir, tell me the name by which you want to save this file")
                 name = takecommand().lower()
                 name1 = name + ".txt"
                 with open(name1, 'w') as file:
                     file.write(writes)

                 path1 = "C:\\Users\\PRAGYA\\Desktop\\Jarvis AI\\" + str(name1)
                 path2 = "C:\\Users\\PRAGYA\\Desktop\\notes\\" + str(name1)
                 os.rename(path1, path2)
                 os.startfile(path2)
            elif 'open facebook' in query:
                speak("Opening Facebook Sir...")
                os.startfile("htpps://www.facebook.com")
                a = False
            elif 'sleep for' in query:
                if 'minutes' in query:
                    query = query.replace('sleep for', "")
                    query = query.replace('minutes', "")
                    if 'minute' in query:
                        query = query.replace('minute', "")
                    if 'jarvis' in query:
                        query = query.replace('jarvis', "")
                    query = int(query)
                    speak(f"Going in Sleep Mode for {query} Minutes Sir")
                    a = False
                    query *= 60
                    print("In Sleep")
                    sleep(query)
                    print("Awake")
                    speak("Waking Up Sir!")
                    a = True
                    query = str(query)
                if 'seconds' in query:
                    query = query.replace('sleep for', "")
                    query = query.replace('seconds', "")
                    if 'second' in query:
                        query = query.replace('second', "")
                    if 'jarvis' in query:
                        query = query.replace('jarvis', "")
                    query = int(query)
                    speak(f"Going in Sleep Mode for {query} Seconds Sir")
                    a = False
                    print("In Sleep")
                    sleep(query)
                    print("Awake")
                    speak("Waking Up Sir!")
                    a = True
                    query = str(query)
            elif 'goodnight jarvis' in query:
                speak("Good Night Sir! Shutting Down")
                quit()
            elif 'my identity' in query:
                speak("You are Pratyush Kumar, My Creator")
                speak("You Study in Class 7 and Are a Good Programmer")
                a = False
            elif 'introduce yourself' in query:
                speak("I am Jarvis, a Advance Artificial Intelligence That will Manage Your Managements, Shedules")
                speak("Apps and Many More Things of Your PC and Will Help you in Anyway!")
                speak("My Owner is You, Pratyush Kumar, My Founder is Mr Stark also known as Tony Stark")
                a = False
            if 'exit' in query:
                speak("Shutting Down, Thank You Sir!")
                query = query.replace('exit', "")
                quit()


    for x in range(1, 10000):
        wake = 'jarvis'
        wake2 = 'wake up'
        while a == False:
            print("Listening")
            print(a)
            text = get_audio()
            print(text)
            if text.count(wake.lower()) > 0 or text.count(wake.lower()) > 0:
                speak("Yes Sir?")
                a = True
        while a == True:
            query = takecommand().lower()
            if 'wikipedia' in query:
                speak("Searching Wikipedia...")
                query = query.replace('wikipedia', "")
                results = wikipedia.summary(query, sentences=2)
                speak("According To Wikipedia")
                print(results)
                speak(results)
                a = False
            elif 'hello jarvis' in query:
                speak("Hello Sir, I am Great How was Your Day")
                query = takecommand().lower()
                speak("Awsome Sir! You Shall Focus on Your Exams!")
                a = False
            elif 'send facebook message' in query:
                speak("Sir for sending a Message, See the Console and Type the Info Please!")
                username = input("Username: ")
                client = fbchat.Client(username, getpass())
                no_of_friends = int(input("Number of friends: "))
                for i in range(no_of_friends):
                    name = input("Name: ")
                    friends = client.searchForUsers(name)  # return a list of names
                    friend = friends[0]
                    msg = input("Message: ")
                    sent = client.sendMessage(msg, thread_id=friend.uid)
                    if sent:
                        speak("Message sent succesfully Sir")
                        print("Message sent successfully!")
                a = False
            elif 'open youtube and search' in query:
                speak("Openning Youtube!")
                query = query.replace('open youtube and search', "")
                if 'jarvis' in query:
                    query = query.replace('jarvis', "")
                webbrowser.open(f'https://youtube.com/results?search_query={query}')
                a = False
            elif 'my location' in query:
                speak("Heres Your Location Sir ")
                webbrowser.open("https://www.google.com/maps/place/Swarnjyoti+Colony,+Bistupur,+Jamshedpur,+Jharkhand+831005"
                         + "/@22.7940679,86.1709209,17z/data=!4m5!3m4!1s0x39f5e49e7b967d41:0x893282463d39ccc7!8m2!3d22."
                          + "7940679!4d86.1731096")
                a = False
            elif 'close Google' in query:
                speak("Closing Google Sir...")
                os.system("TASKKILL /F /im chrome.exe")
                a = False
            elif 'open website' in query:
                query = query.replace('open website', "")
                query = query.replace('jarvis', "")
                query = query.replace(' ', "")
                webbrowser.open(f'https://www.{query}.com')
                a = False
            elif 'open settings' in query:
                speak("Opening Settings...")
                webbrowser.open('chrome://settings/?search=passwords')
                a = False
            elif 'send long message' in query:
                query = query.replace('send message', "")
                query = query.replace('jarvis', "")
                speak("Tell Me The Name of The Person Sir")
                query7 = str(takecommand().lower())
                print(query7)
                if 'papa' in query7:
                    speak("Tell me The Message")
                    query0 = takecommand().lower()
                    while 'none' in query0:
                        speak("Tell me The Message")
                        query0 = takecommand().lower()
                    speak("Tell me the current Hour Sir")
                    query1 = takecommand()
                    if 'Tu' in query1:
                        query1 = 2
                    speak("Now Tell me the current Minute Sir")
                    query2 = int(takecommand())
                    pywhatkit.sendwhatmsg("+919934360377", query0, query1, query2, 10)
                    speak("Sending Whatsapp Message To Papa Sir")
                if 'didi' in query7 or 'pragya' in query7:
                    speak("Tell me The Message")
                    query08 = takecommand().lower()
                    while 'none' in query08:
                        speak("Tell me The Message")
                        query08 = str(takecommand().lower())
                    speak("Tell me the current Hour Sir")
                    query1 = takecommand()
                    if 'Tu' in query1:
                        query1 = 2
                    speak("Now Tell me the current Minute Sir")
                    query2 = int(takecommand())
                    pywhatkit.sendwhatmsg("+917091500107", query08, query1, query2, 10)
                while not 'papa' in query7 or not 'pragya' in query7 or not 'didi' in query7:
                    speak("Tell Me The Name of The Person Sir")
                    query7 = str(takecommand().lower())
                    if 'papa' in query7:
                        speak("Tell me The Message")
                        query0 = takecommand().lower()
                        while 'none' in query0:
                            speak("Tell me The Message")
                            query0 = takecommand().lower()
                        speak("Tell me the current Hour Sir")
                        query1 = takecommand()
                        if 'Tu' in query1:
                            query1 = 2
                        speak("Now Tell me the current Minute Sir")
                        query2 = int(takecommand())
                        pywhatkit.sendwhatmsg("+919934360377", query0, query1, query2, 10)
                        speak("Sending Whatsapp Message To Papa Sir")
                        a = False
                    if 'didi' in query7 or 'pragya' in query7:
                        speak("Tell me The Message")
                        query08 = takecommand().lower()
                        while 'none' in query08:
                            speak("Tell me The Message")
                            query08 = str(takecommand().lower())
                        speak("Tell me the current Hour Sir")
                        query1 = takecommand()
                        if 'Tu' in query1:
                            query1 = 2
                        speak("Now Tell me the current Minute Sir")
                        query2 = int(takecommand())
                        pywhatkit.sendwhatmsg("+917091500107", query08, query1, query2, 10)
                a = False
            elif 'send a message' in query:
                query.replace("send whatsapp message", "")
                query.replace("jarvis", "")
                speak("Type the nummber in the conolse sir")
                num = input("Type Number:")
                m_num = "+91" + num
                speak("Type your message sir")
                msg = input("/nType Message: ")
                open_chat = 'https://web.whatsapp.com/send?photo=' + m_num + '&text=' + msg
                webbrowser.open(open_chat)
                sleep(120)
                keyboard.press('enter')
                a = False
            elif 'open my school notes' in query:
                speak("Opening Your school Notes Sir...")
                os.startfile("C:\\Users\\PRAGYA\\Desktop\\myschool_notes.txt")
                a = False
            elif "what should i do" in query:
                weekday = datetime.datetime.now().strftime(f"%A")
                speak(f"checking about {weekday.lower()}...")
                sleep(3)
                print(weekday)
                weeeedays = ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday"]
                if weekday.lower() in weeeedays:
                   from weekdaytable import Time
                   value = Time()
                   noti1 = Notify()
                   noti1.title = "Weekday Timetable"
                   noti1.message = str(value)
                   noti1.send()
                else:
                   from sundaytable import Time as Time1
                   value1 = Time1()
                   noti2 = Notify()
                   noti2.title = "Sunday Timetable"
                   noti2.message = str(value1)
                   noti2.send()
                a = False
            elif "initiate mark 2" in query:
                speak("activiting Protocol mark 2")
                speak("starting Web scraping test")
                URL = "https://www.google.com/search?q=biology&sxsrf=ALiCzsb43iDHharwPH4j3jKfTksXVKM9Wg%3A1656755074" \
                      "344" \
                      "&" \
                      "ei=ghPAYrrSFMnl4-EPgvEf&oq=bio&gs_lcp=Cgdnd3Mtd2l6EAEYADIECCMQJzIECCMQJzIFCAAQkQIyCAgAEIAEEL" \
                      "EDMgUIABCABDIFCAAQsQMyBQgAEIAEMgUIABCxAzIFCAAQsQMyCAgAEIAEELEDOgcIIxDqAhAnOgQILhAnOgQIABBDOg4" \
                      "ILhCABBCxAxDHARDRAzoICC4QgAQQsQM6CAgAELEDEIMBOgsIABCABBCxAxCDAUoECEEYAEoECEYYAFA" \
                      "AWIMKYI8naAFwAX" \
                      "gAgAHiAYgBqQSSAQUwLjIuMZgBAKABAbABCsABAQ&sclient=gws-wiz"
                page = requests.get(URL)

                soup = BeautifulSoup(page.content, "html.parser")
                speak("Printed soup")
                speak("protocol ended")
            elif "tell" in query:
                print("entered")
                import wikipedia as googleScrap
                if "jarvis" in query:
                    query = query.replace("jarvis", "")
                if "Jarvis" in query:
                    query = query.replace("Jarvis", "")
                query = query.replace("tell me", "")
                speak("Searching google for your search...")
                sleep(3)
                pywhatkit.search(query)
                try:
                    result = googleScrap.summary(query, 5)
                    speak(result)
                    a = False
                except:
                    speak("No Speakable Result")
                    speak("You shall see yourself sir")
                    speak("Opening your result in chrome sir")
                    webbrowser.open(f'https://www.google.com/search?q={query}')
                    a = False
            elif 'search' in query:
                speak("Searching...")
                query = query.replace('search', "")
                if 'jarvis' in query:
                    query = query.replace('jarvis', "")
                speak('Here are The Results I found:')
                webbrowser.open(f'https://www.google.com/search?q={query}')
                a = False
            elif 'open youtube' in query:
                speak("Openning Youtube!")
                query = query.replace('open youtube', "")
                webbrowser.open(f'https://youtube.com')
                a = False
            elif 'pause' in query:
                speak('video Paused sir')
                keyboard.press('space bar')
                a = False
            elif 'play' in query:
                speak("playing the video sir")
                keyboard.press('space bar')
                a = False
            elif 'mute' in query:
                speak("Video  Muted Sir")
                keyboard.press('m')
                a = False
            elif 'unmute' in query:
                speak('ok sir, video unmuted')
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
            elif "reboot yourself" in query:
                speak("rebooting")
                keyboard.press("shift")
                keyboard.press("f10")
                keyboard.release("shift")
                keyboard.release("f10")
            elif 'restart' in query:
                keyboard.press('0')
                a = False
            elif 'Close tab' in query:
                keyboard.press("ctrl")
                keyboard.press("w")
                keyboard.release("ctrl")
                keyboard.release("w")
                a = False
            elif 'Open new tab' in query:
                keyboard.press("ctrl")
                keyboard.press("t")
                keyboard.release("ctrl")
                keyboard.release("t")
                a = False
            elif query.startswith("close it"):
                speak("Closing application")
                keyboard.press("alt")
                keyboard.press("f4")
                keyboard.release("alt")
                keyboard.release("f4")
                a = False
            elif 'joke' in query:
                joke = pyjokes.get_joke()
                speak("heres a Joke for you sir")
                speak(joke)
                a = False
            elif 'open google' in query:
                speak("Opening Chrome...")
                app = 'C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe'
                subprocess.Popen(app)
                a = False
            elif 'open discord' in query:
                speak("Opening Web Discord...")
                webbrowser.open(f'https://discord.com/')
                a = False
            elif 'who is my sister' in query:
                speak(
                    "Your Sister is Pragya Priyadarshini, She is 23 Years Old, She is a Bright Student and She wants to"),
                speak("be a Docter, She is Trying For it from Many years and Has Reached On a Master Level, She Likes")
                speak(
                    "Paneer and Chicken The Most and As most girls, she has Everything Fucking PINK. She Loves Biology")
                speak(
                    "She Doesnt Give a Shit About Her COOL DASHING Brother, My owner. He hopes she will play with her")
                speak("After her College Entrence. She works Very Hard for it")
                speak("And I Jarvice is pretty Sure that she will make it to be a docter,Dont be offended")
                a = False
            elif 'who is my father' in query:
                speak('Sir, Your Father is Pradip Kumar Mishra, He is 56 Years Old. He works in Goods and Services'),
                speak('Taxes (GST), a Govermental Job in Which he is a Supritendent of Tribunal Review. He likes'),
                speak(' Classic Music and He doesnt leaves a shopping store quickly. he likes sweets as he is sweet '),
                speak('and He is` the best dad I jarvis has seen ever')
                a = False
            elif 'type word' in query:
                query = query.replace('type word', "")
                query = query.replace('jarvis', "")
                query.upper()
                keyboard = Controller()
                key = f"{query}"

                keyboard.press(key)
                keyboard.release(key)
                a = False
            elif 'set alarm' in query:
                inp = '07:05:00'
                hgu = '07:05:45'
                speak("alarm set sir")
                y = True
                while True:
                    nowt = datetime.datetime.now().strftime('%H:%M:%S')
                    if inp == nowt or inp <= nowt:
                        speak("Wake Up Sir...")
                        playsound("C:\\Users\\PRAGYA\\Music\\Music\\alarm_music.mp3")
                        speak("Sir its a Important Day, You shall study now")
                        playsound("C:\\Users\\PRAGYA\\Music\\Music\\alarm_music.mp3")
                        speak("Sir its a Important Day, You shall study now")
                        playsound("C:\\Users\\PRAGYA\\Music\\Music\\alarm_music.mp3")
                        speak("Alarm Closed Sir")
                        quit()
                a = False
            elif 'check internet speed' in query:
                import speedtest
                speed = speedtest.Speedtest()
                downloading = speed.download()
                correctdown = int(downloading/800000)
                uploading = speed.upload()
                correctupload = int(uploading/800000)
                if 'uploading' in query:
                    speak("Checking Uploading Speed...")
                    speak(3)
                    speak(f"The Uploading Speed Of Your WiFi is {correctupload}")
                elif 'downloading' in query:
                    speak("Checking Downloading Speed...")
                    speak(3)
                    speak(f"The Downloading Speed Of Your WiFi is {correctdown}")
                else:
                    speak("Checking The Speed...")
                    sleep(3)
                    speak(f"The Uploading Speed Of Your WiFi is {correctupload} and The Downloading Speed Of Your WiFi "
                          f"is {correctdown}")
                a = False
            elif 'open dictionary' in query:
                speak("Opening Dicrionary For You Sir...")
                speak("Please Tell What is Your Problem...")
                b1 = takecommand().lower()
                if 'meaning' in b1:
                    b1 = b1.replace("meaning", "")
                    result = dict.meaning(b1)
                    speak(f"The Meaning of {b1} is {result}.")
                if 'antonym' in b1:
                    b1 = b1.replace("antonym", "")
                    result = dict.antonym(b1)
                    speak(f"The Antonym of {b1} is {result}.")
                if 'synonym' in b1:
                    b1.replace("synonym", "")
                    result = dict.synonym(b1)
                    speak(f"The Synonym of {b1} is {result}.")
                a = False
            elif 'leave message' in query:
                query = query.replace('leave message', "")
                query = query.replace('jarvis', "")
                while True:
                    speak(query)
                    sleep(10)
                a = False
            elif 'close Google' in query:
                speak("Closing Google Sir...")
                os.system("TASKKILL /F /im chrome.exe")
                a = False
            elif 'music' in query:
                speak("Here is the List of Music! You shall Look in the Console for Text Sir!")
                query = query.replace('play music', '')
                music_dir = 'C:\\Users\\PRAGYA\\Music\\Music'
                songs = os.listdir(music_dir)
                print("Current Songs:")
                print(songs)
                speak("Tell Which Song to Play By Number")
                print("Tell Which Song to Play By Number")
                query1 = takecommand().lower()
                if 'tu' in query1:
                    query1 = query1.replace('tu', '2')
                query1 = int(query1)
                query1 -= 1
                y = songs[query1]
                a = False
                os.startfile(os.path.join(music_dir, songs[query1]))
                print("Currently Playing: " + songs[0])
            elif "remember that" in query:
                rmbMsg = query.replace("remember that", "")
                if 'jarvis' in query:
                  rmbMsg = rmbMsg.replace("jarvis", "")
                speak("Ok sir I will remember that, " + rmbMsg)
                remember = open("reminder.txt", "w")
                remember.write(rmbMsg)
                remember.close()
                a = False
            elif "repeat after me" in query:
                speak("Just say the word to repeat sir and say stop jarvis when to stop")
                rep = takecommand().lower()
                while rep != "stop jarvis":
                    speak(rep)
                    rep = takecommand().lower()
                speak("ok sir")
                a = False
            elif "what do you remember" in query:
                with open('reminder.txt') as f:
                    remember = f.readlines()
                    speak("You told me to remember that " + remember[0])
                    a = False
            elif "temperature" in query:
                query = query.replace("temperature in", "")
                if 'what is the' in query:
                    query = query.replace("what is the", "")
                if "jarvis" in query:
                    query = query.replace("jarvis", "")
                if 'Jarvis' in query:
                    query = query.replace("Jarvis", "")

                api_key = "03fb7ccae2cc1facf6714847a6370b26"

                # base_url variable to store url
                base_url = "http://api.openweathermap.org/data/2.5/weather?"

                # Give city name
                city_name = query
                print(f"City: {city_name}")

                # complete_url variable to store
                # complete url address
                complete_url = base_url + "appid=" + api_key + "&q=" + city_name

                # get method of requests module
                # return response object
                response = requests.get(complete_url)

                # json method of response object
                # convert json format data into
                # python format data

                x = response.json()


                # Now x contains list of nested dictionaries
                # Check the value of "cod" key is equal to
                # "404", means city is found otherwise,
                # city is not found

                if x["cod"] != "404":

                    # store the value of "main"
                    # key in variable y
                    y = x["main"]

                    # store the value corresponding
                    # to the "temp" key of y
                    current_temperature = y["temp"]
                    temp_in_c = current_temperature - 273.15
                    print(f"Temperature: {int(temp_in_c)} degree C")
                    # store the value corresponding
                    # to the "pressure" key of y
                    current_pressure = y["pressure"]
                    print(f"Air Pressure: {current_pressure} hactopascal")

                    # store the value corresponding
                    # to the "humidity" key of y
                    current_humidity = y["humidity"]
                    print(f"Humidity: {current_humidity}%")

                    # store the value of "weather"
                    # key in variable z
                    z = x["weather"]

                    # store the value corresponding
                    # to the "description" key at
                    # the 0th index of z
                    weather_description = z[0]["description"]
                    speak(f"Sir, Todays Temperature in {query} is {int(temp_in_c)} degree celsius, The Pressure is"
                          f" {current_pressure} hactopascal, and the Humidity is {current_humidity}%, And"
                          f" Its {weather_description} Sir, Thats it Sir")
                a = False
            elif 'reminders' in query:
                speak("Sir You had to")
                speak("1 Do your Physics Copy Work")
                speak('2 your Bio work')
                speak("3 Your Maths Project and Practise")
                speak('4 Stick project pics')
                speak("5 Do the Sign and Symbols")
                speak("6 Learn English Language Speech")
                a = False
            elif "what is today's news on" in query:
                topic = query.replace("what is today's news on ", "")
                speak(f"Checking Latest Hot News for {topic}")
                sleep(5)
                from gnewsclient import gnewsclient

                client = gnewsclient.NewsClient(language='english',
                                                location='india',
                                                topic=topic.lower(),
                                                max_results=5)

                news_list = client.get_news()

                for item in news_list:
                    print("Title : ", item['title'])
                    speak(f"{item['title']}")
                    print("")
                speak("sir do you want more news?")
                yn = takecommand().lower()
                while "ok" in yn or "no" in yn or "yes" in yn:
                    if "ok" in yn:
                        speak("ok sir, checking more news")
                        sleep(5)
                        client = gnewsclient.NewsClient(language='english',
                                                        location='india',
                                                        topic=topic.lower(),
                                                        max_results=5)

                        news_list = client.get_news()

                        for item in news_list:
                            print("Title : ", item['title'])
                            speak(f"{item['title']}")
                            print("")
                        speak("sir do you want more news?")
                        yn = takecommand().lower()
                    elif "yes but on" in yn:
                        yn = yn.replace("yes but on", "")
                        print(yn)
                        speak("ok sir, checking more news for new topic")
                        sleep(5)
                        client2 = gnewsclient.NewsClient(language='english',
                                                         location='india',
                                                         topic= yn.lower(),
                                                         max_results=5)

                        news_list = client2.get_news()

                        for item in news_list:
                            print("Title : ", item['title'])
                            speak(f"{item['title']}")
                            print("")
                        speak("sir do you want more news?")
                        yn = takecommand().lower()
                    else:
                        speak("ok sir, thanks for eharing the news!")
                        a = False
            elif 'good morning' in query:
                strtime = datetime.datetime.now().strftime(f"%H")
                hour = int(datetime.datetime.now().hour)
                speak("Good Morning Sir, Today is a Wonder Full Day and Its {hour}`o clock Sir, You shall Study")
                a = False
            elif 'tell my remaining projects' in query:
                speak(
                    "Sir, You have 4 Projects Remaing, of Maths, Physics, Chemistry and Biology, You shall Do CHemistry")
                speak("First Sir! You have to Write Table 1 of 30 Elements and About Thier Element Name and Symbol and")
                speak("Thier Atomic Number")
                speak("and Thier Mass Number and Number of Electrons, Protons and Nutrons Also Sir")
                speak("In Table 2 You have to Differntiate the elements  all 30 in Metals, Non metals and Metaloids Sr")
                speak(
                    "In Table 3 ou have To Write Formulas of 50 Compunds given in Page Number 42 in Chemistry Main Book")
                speak("and also in Page number 21 of Chemical Communication Book, You have to write the formula with")
                speak("cris-cross method like in the rough copy. Then, You have write the Elctron Confrigation of All")
                speak(" 30 Elements like how manyy electron in K shell, L shell, M shell and N Shell! Thats It Sir")
                sleep(3)
                speak("Do you want me to Repeat Sir?")
                query = takecommand().lower()
                if 'yes' in query:
                    while 'yes' in query:
                        speak(
                            "Sir, You have 4 Projects Remaing, of Maths, Physics, Chemistry and Biology, You shall Do CHemistry")
                        speak(
                            "First Sir! You have to Write Table 1 of 30 Elements and About Thier Element Name and Symbol and")
                        speak("Thier Atomic Number")
                        speak("and Thier Mass Number and Number of Electrons, Protons and Nutrons Also Sir")
                        speak(
                            "In Table 2 You have to Differntiate the elements  all 30 in Metals, Non metals and Metaloids Sir")
                        speak(
                            "In Table 3 you have To Write Formulas of 50 Compunds given in Page Number 42 in Chemistry Main Book")
                        speak(
                            "and also in Page number 21 of Chemical Communication Book, You have to write the formula with")
                        speak(
                            "cris-cross method like in the rough copy. Then, Table 4 is You have write the Elctron Confrigation of All")
                        speak(
                            " 30 Elements like how manyy electron in K shell, L shell, M shell and N Shell! Thats It Sir")
                        speak("do you want me to repeat again sir?")
                        query = takecommand().lower()
                if 'no' in query:
                    speak("ok sir")
                    speak("You Shall Study Now Sir, Going in Stand By Mode")
                    a = False
                a = False
            elif "what is the time" in query:
                strtime = datetime.datetime.now().strftime(f"%H:%M")
                hour = int(datetime.datetime.now().hour)
                if hour >= 0 and hour < 12:
                    speak(f"Sir, the time is {strtime} AM , Good Morning!")
                elif hour >= 12 and hour < 18:
                    speak(f"Sir, the time is {strtime} PM , Good AFternoon!")
                elif hour >= 18 and hour < 21:
                    speak(f"Sir, the time is {strtime} PM , Good Evening!")
                else:
                    speak(f"Sir, the time is {strtime} PM , Good Night!")
                print(f"Sir, the time is {strtime}")
                a = False
            elif "what is today's date" in query:
                strdate = datetime.datetime.now().strftime(f"%d %B")
                weekday = datetime.datetime.now().strftime(f"%A")
                speak(f"Sir todays date is {strdate} and its {weekday}")
            elif 'open classroom' in query:
                speak("Opening Google Classroom Sir...")
                webbrowser.open('https://classroom.google.com/u/0/h')
                a = False
            elif 'thank you' in query:
                speak("No Probem Sir!")
                a = False
            elif 'go in standby mode' in query or 'go to sleep' in query:
                speak("Going in Stand By Mode Sir, Please Say Jarvis For Returning Me Back To Active Mode")
                a = False
            elif "note in notepad" in query:
                 speak("Sir, Just tell me what to write")
                 writes = takecommand().lower()
                 speak("sir, tell me the name by which you want to save this file")
                 name = takecommand().lower()
                 name1 = name + ".txt"
                 with open(name1, 'w') as file:
                     file.write(writes)

                 path1 = "C:\\Users\\PRAGYA\\Desktop\\Jarvis AI\\" + str(name1)
                 path2 = "C:\\Users\\PRAGYA\\Desktop\\notes\\" + str(name1)
                 os.rename(path1, path2)
                 os.startfile(path2)
            elif 'open YouTube history' in query:
                speak("Opening Your Youtube History Sir")
                webbrowser.open('https://www.youtube.com/feed/history')
                a = False
            elif 'open WhatsApp' in query:
                speak("Opening Whatsapp Sir...")
                webbrowser.open('https://web.whatsapp.com/')
                speak("You shall Check the messages sir")
                a = False
            elif 'open facebook' in query:
                speak("Opening Facebook Sir...")
                os.startfile("https://www.facebook.com")
                a = False
            elif 'sleep for' in query:
                if 'minutes' in query:
                    query = query.replace('sleep for', "")
                    query = query.replace('minutes', "")
                    if 'minute' in query:
                        query = query.replace('minute', "")
                    if 'jarvis' in query:
                        query = query.replace('jarvis', "")
                    query = int(query)
                    speak(f"Going in Sleep Mode for {query} Minutes Sir")
                    a = False
                    query *= 60
                    print("In Sleep")
                    sleep(query)
                    print("Awake")
                    speak("Waking Up Sir!")
                    a = True
                    query = str(query)
                if 'seconds' in query:
                    query = query.replace('sleep for', "")
                    query = query.replace('seconds', "")
                    if 'second' in query:
                        query = query.replace('second', "")
                    if 'jarvis' in query:
                        query = query.replace('jarvis', "")
                    query = int(query)
                    speak(f"Going in Sleep Mode for {query} Seconds Sir")
                    a = False
                    print("In Sleep")
                    sleep(query)
                    print("Awake")
                    speak("Waking Up Sir!")
                    a = True
                    query = str(query)
            elif 'goodnight jarvis' in query:
                speak("Good Night Sir! Shutting Down")
                quit()
            elif 'my identity' in query:
                speak("You are Pratyush Kumar, My Creator")
                speak("You Study in Class 7 and Are a Good Programmer")
                a = False
            elif 'introduce yourself' in query:
                speak("I am Jarvis, a Advance Artificial Intelligence That will Manage Your Managements, Shedules")
                speak("Apps and Many More Things of Your PC and Will Help you in Anyway!")
                speak("My Owner is You, Pratyush Kumar, My Founder is Mr Stark also known as Tony Stark")
                a = False
            if 'exit' in query:
                speak("Shutting Down, Thank You Sir!")
                query = query.replace('exit', "")
                quit()
#add chand waliyan music
#add ratan lambiyan music
#make a routine system also so it will tell what to do at a time
#make it say what are the main results on google