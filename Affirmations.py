#Made by Xanthus58 https://github.com/Xanthus58

#Defines often used code for a little bit of cleanup
def t5():
    time.sleep(.5)
def cls():
    os.system('cls||clear')
def enter():
    print("")
def intro():
    print('Hold A for an affirmation')
    enter()
    print("Hold I For an image based, AI generated affirmation")
    enter()
    print("Hold M for a mean insult")
    enter()
    print("Hold Q to exit")
    enter()
    print("Hold C for credits")
    enter()
    print("Hold Z to choose a colour")
    enter()
#imports required code prereqesets
import requests
import keyboard
import time
import os
import webbrowser
from colorama import Fore, Back, Style
#Explains how to use the application
intro()
#Makes a repeating loop for the code
while True:
    #If the user presses "A" it will make a get request to an affirmation API
    if keyboard.read_key() == "a":
        #Displays the Fetching animation
        cls()
        print('Fetching')
        t5()
        cls()
        print('Fetching.')
        t5()
        cls()
        print('Fetching..')
        t5()
        cls()
        print('Fetching...')
        #Requests and Displays the affirmation
        affirmation = requests.get('https://www.affirmations.dev/')
        s1=affirmation.text
        s2=s1.replace("{","")
        s3=s2.replace("}","")
        s4=s3.replace(":","")
        s5=s4.replace("affirmation","")
        s6=s5.strip('"',)
        cls()
        print(s6)
        time.sleep(5)
        cls()
        intro()
    #If the user presses "I" It will make an api request to generate an affirmation
    elif keyboard.read_key() == "i":
        #Displays the Generating animation
        cls()
        print('Generating')
        t5()
        cls()
        print('Generating.')
        t5()
        cls()
        print('Generating..')
        t5()
        cls()
        print('Generating...')
        #Requests and prints the affirmation
        affirmation = requests.get('https://inspirobot.me/api?generate=true')
        s1=affirmation.text
        cls()
        print(s1)
        webbrowser.open(s1)
        enter()
        print("Please check your web browser; the image should be open. If not follow the steps below")
        enter()
        print("If your using the windows terminal press control and left click to follow the link.")
        print("Otherwise Copy and paste the link into your web browser")
        time.sleep(7)
        cls()
        intro()
    elif keyboard.read_key() == "m":
        #Displays the Generating animation
        cls()
        print('Fetching')
        t5()
        cls()
        print('Fetching.')
        t5()
        cls()
        print('Fetching..')
        t5()
        cls()
        print('Fetching...')
        #Requests and prints the insult
        affirmation = requests.get('https://evilinsult.com/generate_insult.php?lang=en')
        s1=affirmation.text
        cls()
        print(s1)
        time.sleep(5)
        cls()
        intro()
    #Detects if the user presses Z and shows all of the colour options
    elif keyboard.read_key() == "z":
        cls()
        print(Fore.RED +"Hold R for the colour Red")
        print(Fore.BLUE + "Hold B for the colour Blue")
        print(Fore.GREEN + "Hold G for the colour Green")
        print(Fore.YELLOW + "Hold Y for the colour Yellow")
        print(Fore.WHITE)
        time.sleep(1)
    #If the user presses one of the colour buttons on the main menu; or colour menu. It will change the text to be that colour!
    elif keyboard.read_key() == "r":
        cls()
        print(Fore.RED + "You have chosen the colour red!")
        time.sleep(5)
        cls()
        intro()
    elif keyboard.read_key() == "y":
        cls()
        print(Fore.YELLOW + "You have chosen the colour Yellow!")
        time.sleep(5)
        cls()
        intro()
    elif keyboard.read_key() == "b":
        cls()
        print(Fore.BLUE + "You have chosen the colour blue!")
        time.sleep(5)
        cls()
        intro()
    elif keyboard.read_key() == "g":
        cls()
        print(Fore.GREEN + "You have chosen the colour Green!")
        time.sleep(5)
        cls()
        intro()
    #When "Q" is pressed it will shut down the application.
    elif keyboard.read_key() == "q":
        cls()
        print("I hope you have a wonderful day!")
        time.sleep(5)
        break
    #When "C" is pressed it will show the my credits
    elif keyboard.read_key() == "c":
        cls()
        print("Made by Xanthus In my spare time")
        enter()
        print("Check out my other works at https://github.com/Xanthus58")
        enter()
        print("Email me on 'Xanthus58@protonmail.com'")
        enter()
        print("Feel free to fork; submit issues; or otherwise interact with the project here!")
        print("https://github.com/Xanthus58/Affirmation-Requester")
        enter()
        input("Press Enter to return to the main menu.")
        cls()
        intro()
    #If another key is detected it asks for a propper input
    elif keyboard.read_key() != "a":
        cls()
        print ('Please press "A" for an affirmation "Q" to exit or "Z" For a colour')
        time.sleep(5)
        cls()
        intro()