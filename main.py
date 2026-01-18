from functions import *
import time
import os

name, age, gender, restricted = None, None, None, None

def introduction():
    global name, age, gender, restricted
    narrate("Welcome to Fate! This is a CYOA (Choose Your Own Adventure) game where you make your own decisions")
    narrate("and the story ends up different for everyone!")
    print("\n")
    narrate("First, let's set up some things. We have a few questions, and then we can start the story!")
    print()
    narrate("What gender are you attracted to? This is required to make the story feel more personal (male/female): ")
    gender = input()
    if gender.lower == "male":
        gender = "F"
    else:
        gender = "M"
    print()
    narrate("Next, what's your name?: ")
    name = input()
    print()
    narrate("Third, your age?: ")
    age = input()
    if int(age) > 12:
        restricted = False
    else:
        restricted = True
    narrate("Lastly, what WPM do you read at? This will make reading more comfortable:")
    wpm = int(input())
    print()
    narrate("Type exit at any prompt to save and stop the story at any time.", wpm)
    time.sleep(0.5)
    narrate("Alright, let's get into the story now!", wpm)

intro = """ _______  _______ _________ _______ 
(  ____ \(  ___  )\__   __/(  ____ \\
| (    \/| (   ) |   ) (   | (    \/
| (__    | (___) |   | |   | (__    
|  __)   |  ___  |   | |   |  __)   
| (      | (   ) |   | |   | (      
| )      | )   ( |   | |   | (____/\\
|/       |/     \|   )_(   (_______/
                                    """

os.system("cls")
print(intro)
time.sleep(2)
if check():
    introduction()
else:
    narrate("Welcome back to Fate! Would you like to continue your previous story or start a new one?")
    print("A) Start new story\nB) Continue previous story")
    if input() == "A":
        introduction()
    else:
        data = load()
        name = data["name"]
        gender = data["gender"]
        restricted = data["age"]
