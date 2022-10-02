from datetime import datetime
import pyttsx3

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
print(voices)
engine.setProperty('voices', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

sixtohalfseven = '''
Sir from 6 am to 8 am You have to Go to School, according to your previous timings, you should be in school by 7 30! You shall Hurry! and
If you are in home for holiday or bunking so you shall study until 11 am or 12 pm

'''

seventoeleven = '''
sir from 8 am to 11 am in this time,you are in school and maybe giving exams or You shall be at home and Shall study till 12 pm
'''

eleventoonepm = '''
Sir from 11 am to 1 pm in this time, you shall be in school and If you are in home, you shall be studing till 1 PM and Eat your Breakfast!
'''

onetothree = """
sir from 1 pm to 3 pm in this time You shall have your lunch and play games or enjoy by watching tv if you have not studied or shall start
 study, 
sir, if you haven studied in morning because of school, You shall extremely study now
"""

threetofive = """Sir from 3 pm to 5 pm In this time you shall watch tv serials with mom and sister and do coding if you want!
"""

fivetoseven = """Sir from 5 pm to 7 pm in this time you shall go outside to play if you want to or study if you havent studied in the
 morning as you were in shcool"""

seventoeight = """
Sir from 7 pm to 8 pm in this time you can do fun if you want and If you haven studied a Little bit since mroning or have on ly studied
at noon and not again after that, you shall study! and should practice Maths! or if you have studied then code me!
"""

eighttoten = """Sir from 8 pm to 10 pm in this you can have any snacks like noodles and eat Dinner if its made, and This is th last study
 period so if your import study material is pending, do it in this time  """

tento12 = """
sir from ten pm to 12 am you shall be going to sleep in this time and wake by 6 30 or 5 30, goodnight and sleep fast!
"""

def Time():
    hour = int(datetime.now().strftime("%H"))
    min = int(datetime.now().strftime("%M"))

    if hour >= 6 and hour <= 8:
        speak(sixtohalfseven)
        return sixtohalfseven
    elif hour >= 8 and hour <= 11:
        speak(seventoeleven)
        return seventoeleven
    elif hour >= 11 and hour <= 13:
        speak(eleventoonepm)
        return eleventoonepm
    elif hour >= 13 and hour <= 15:
        speak(onetothree)
        return onetothree
    elif hour >= 15 and hour <= 17:
        speak(threetofive)
        return threetofive
    elif hour >= 17 and hour <= 19:
        speak(fivetoseven)
        return fivetoseven
    elif hour >= 19 and hour <= 20:
        speak(seventoeight)
        return seventoeight
    elif hour >= 20 and hour <= 22:
        speak(eighttoten)
        return eighttoten
    elif hour >= 22 and hour <= 24:
        speak(tento12)
        return tento12
    else:
        speak(''' You Shall sleep sir''')
