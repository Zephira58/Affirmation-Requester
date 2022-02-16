#Made by Xanthus58 https://github.com/Xanthus58

#imports required code prereqesets
import requests
import keyboard
import time
#Explains how to use the application
print('Press A for an Afformation')
print("")
print("Or press Q to exit")
print("")
#Makes a repeating loop for the code
while True:
    #If the user presses "A" it will make a get request to an afformation API
    if keyboard.read_key() == "a":
        afformation = requests.get('https://www.affirmations.dev/')
        print (afformation.text)
    elif keyboard.read_key() == "q":
        break
    #If another key is detected it asks for a propper input
    elif keyboard.read_key() != "a":
        print ('Please press "A" for an afformation or "Q" to exit')
    #If the code breaks it closes the application
    else:
        print("Some internal error has occured, the application will now exit")
        time.sleep(5)
        break