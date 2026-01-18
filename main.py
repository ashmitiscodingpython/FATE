from functions import *
import time
import os

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
narrate("Welcome to Fate! This is a CYOA (Choose Your Own Adventure) game where you make your own decisions")
narrate("and the story ends up different for everyone!")
print("\n")
narrate("First, let's set up some things. We have a few questions, and then we can start the story!")
print("")
narrate("What is your gender? This is required to make the story feel more personal (male/female): ")
gender = input()
if gender.lower == "male":
    gender = 0
else:
    gender = 1
print("")
narrate("Next, what's your name?: ")
name = input()
print("")
narrate("Third, your age?: ")
age = input()
if age > 12:
    restricted = False
else:
    restricted = True
