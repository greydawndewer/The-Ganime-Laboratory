from datetime import datetime
import pyttsx3

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
print(voices)
engine.setProperty('voices', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

eigthtonine = '''
Sir in this time you shall be awaken and should fresh up by 9
'''

ninetoeleven = '''
sir in this time, you can study if you want or have ome morning snakcs or breakfast or code
'''

eleventoonepm = '''
Sir in this time, you can play games and code if you have studied or study science!
'''

onetothree = """
sir in this time You shall have your lunch and play games or enjoy by watching tv, if you have not studied
 you shall start
 study, 
sir, if you havent studied in morning, You shall extremely study now
"""

threetofive = """Sir In this time you shall watch tv serials with mom and sister and do coding if you want! or have 
lunch if you havent
"""

fivetoseven = """Sir in this time you shall go outside to play if you want to or study if you havent studied in the
 morning, you can code also"""

seventoeight = """
Sir in this time you can do fun if you want and If you havent studied a Little bit since mroning or have only studied
at noon and not again after that, you shall study! and should practice Maths! or if you have studied then code me!
"""

eighttoten = """Sir in this time you can have any snacks like noodles and eat Dinner if its made, and This is the last
 study
 period so if your important study material is pending, do it in this time  """

tento12 = """
sir you shall be sleeping in this time and wake by 6 30 or 5 30, goodnight!
"""

def Time():
    hour = int(datetime.now().strftime("%H"))