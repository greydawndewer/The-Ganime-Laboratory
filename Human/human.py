
import os
import sys

global heart_beat


class Organ(object): # the main class
    age = 0
    organ_online = True
    organ_health = 100

    def __init__(self, name, functionality):
        self.name = name
        self.functionality = functionality


class SenseOrgan(Organ): # not used
    def __init__(self, name, functionality, info_input):# organ class, INHERIT from organ parent class
        self.info_input = info_input


class Brain(Organ):
    def __init__(self, name, functionality, brain_iq, brain_sharpness, heart):
        self.brain_iq = brain_iq
        self.brain_sharpness = brain_sharpness
        print("Brain Alive")
        with open('heart_beat.txt') as f:
            lines = f.read()
            heart_beat = lines
            print(heart_beat)
        if (heart_beat == 60 * x for x in range(1, 101)):
            self.age += 1

    def go(self, place):
        skeleton.locomote(place)

    def pick(self, thing):
        skeleton.take_in_hand(thing)


class Heart(Organ):
    def __init__(self, name, functionality, blood_pressure, lungs, brain, skeleton):
        self.blood_pressure = blood_pressure
        if self.age < 20:
            blood_pressure = 0
        if brain == True:
            pass
        else:
            print("Heart Died Because of Non Existence of Brain")
            sys.exit()
        if lungs == True:
            print("Heart Alive")
            pass
        else:
            print("Heart Died Because of Non Existence of Lungs")
            sys.exit()
        with open('heart_beat.txt') as f:
            lines = f.read()
            heart_beat = lines
        x = heart_beat
        if (heart_beat == 60 * x :
            self.age += 1


class Lungs(Organ):
    def __init__(self, name, functionality, heart, brain):
        print("Lungs Alive")
        with open('heart_beat.txt') as f:
            lines = f.readlines()
            heart_beat = lines
        if (heart_beat == 60 * x for x in range(1, 101)):
            self.age += 1
        if (brain == True):
            pass
        else:
            print("Lungs Died Because of Non Existence of Brain")
            quit()


class Skeleton(Organ):
    def __init__(self, name, functionality, bones, brain):
        self.bones = bones
        if (brain == True):
            pass
        else:
            print("Skeleton Died Because of Non Existence of Brain")
            quit()

    def locomote(self, place):
        print(f"Going -  {place}")

    def take_in_hand(self, thing):
        print(f"Picking -  {thing}")


heart = 1
brain = Brain("Brain", "Operates The Full Body Functions", 108, 69, heart)
if brain != None:
    brain_alive = 1
else:
    print("LOL")
    brain_alive = 0
skeleton = Skeleton("Vessel", "Gives Body Structure, Protection and Helps to Locomote", 206, brain_alive)
lungs = Lungs("Lungs", "Circulates Air in Full Body", heart, brain_alive)
while True:
    lungs_work = 1
    main_heart = Heart("Heart", "Pumps Blood To Full Body", 0, brain_alive, lungs_work, skeleton)
    query = input("Action: ")
    if "Go to " in query:
        query = query.replace("Go to ", "")
        brain.go(query)
        print(brain.age)
    if "Pick" in query:
        query = query.replace("Pick", "")
        brain.pick(query)
        print(brain.age)




