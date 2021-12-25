# personal assistant, nvc empathy bot.
import random
import datetime
from time import sleep
from mod_get_empathy import *
from mod_visualize import *
from mod_is_it_feeling import *
from mod_coda_inventory import *
from mod_coda_inv_review import *

# Write timestamp of program launch
launch_date = open("timestamps/launch_date.txt", "a")
launch_date.write(str(datetime.datetime.now()) + "\n")

# TO DO: Check last login date and comment on how long it has been.

if datetime.datetime.now().hour < 12:
    greeting_time = "Good morning"
elif datetime.datetime.now().hour < 17:
    greeting_time = "Good afternoon"
elif datetime.datetime.now().hour <= 23:
    greeting_time = "Good evening"
else:
    greeting_time = "My, you are up late"

print(greeting_time + " my friend.")
sleep(0.1)

while True:
    print("How would you like to practice?")
    sleep(0.1)
    print("'g' to play the 'is it a feeling?' game.")
    sleep(0.1)
    print("'v' to visualize feelings.")
    sleep(0.1)
    print("'e' to receive empathy.")
    sleep(0.1)
    print("'c' to inventory CoDa patterns.")
    sleep(0.1)
    print("'r' to review CoDa pattern inventories.")

    greeting_response = input()

    if greeting_response == "e":
        sleep(0.1)
        get_empathy()
    elif greeting_response == "g":
        sleep(0.1)
        is_it_feeling()
    elif greeting_response == "c":
        sleep(0.1)
        coda_inventory()
    elif greeting_response == "v":
        sleep(0.1)
        visualize()
    elif greeting_response == "r":
        sleep(0.1)
        coda_inv_review()
    else:
        sleep(0.1)
        print("That's not an option right now.")

    print("Now that we've done that...")
    sleep(0.1)

# To Do:
# Only list the option to inventory CoDa patterns if there is no inventory file already present for the day.
