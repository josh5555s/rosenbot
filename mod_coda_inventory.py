import random
import os
import datetime
from time import sleep
from list_feelings import *
from mod_get_empathy import *

# from feeling_responses import *
from list_coda_patterns import *
from list_yes_or_no import *


def coda_inventory():
    path = f"{os.getcwd()}/coda_inventories/{datetime.datetime.now()}"
    os.mkdir(path)
    print("Let's run through some CoDa patterns.")
    sleep(0.1)
    print(
        "Rate them based on the prominence of their expression in your behavor recently."
    )
    sleep(0.1)
    print("5 = This is a significate dimension of my life.")
    sleep(0.1)
    print("4 = I often notice this.")
    sleep(0.1)
    print("3 = I sometimes notice this.")
    sleep(0.1)
    print("2 = I don't often notice this.")
    sleep(0.1)
    print("1 = This really doesn't apply to me.")
    # TO DO: add review filter for previous ratings of 3+, 4+, only 5s, etc.
    sleep(0.1)
    print("Hit enter when you are ready to begin.")
    input()
    shuffled_patterns = all_coda_patterns
    random.shuffle(shuffled_patterns)
    i = 0  # to cycle through patterns array
    while i < len(shuffled_patterns):
        print(f"Do you {shuffled_patterns[i]}?")
        response = input()

        def rate_item():
            rating = open(f"{path}/{response}s.txt", "a")
            rating.write(f"Do you {shuffled_patterns[i]}?\n")

        def record_catigory():
            if shuffled_patterns[i] in denial_patterns:
                sort = open(f"{path}/denial_patterns.txt", "a")
                sort.write(f"{response} - Do you {shuffled_patterns[i]}?\n")
            elif shuffled_patterns[i] in low_self_esteem_patterns:
                sort = open(f"{path}/low_self_esteem_patterns.txt", "a")
                sort.write(f"{response} - Do you {shuffled_patterns[i]}?\n")
            elif shuffled_patterns[i] in compliance_patterns:
                sort = open(f"{path}/compliance_patterns.txt", "a")
                sort.write(f"{response} - Do you {shuffled_patterns[i]}?\n")
            elif shuffled_patterns[i] in control_patterns:
                sort = open(f"{path}/control_patterns.txt", "a")
                sort.write(f"{response} - Do you {shuffled_patterns[i]}?\n")
            elif shuffled_patterns[i] in avoidance_patterns:
                sort = open(f"{path}/avoidance_patterns.txt", "a")
                sort.write(f"{response} - Do you {shuffled_patterns[i]}?\n")
            else:
                print("Error, something is wrong.")

        if response == "1":
            rate_item()
            record_catigory()
            i = i + 1
        elif response == "2":
            rate_item()
            record_catigory()
            i = i + 1
        elif response == "3":
            rate_item()
            record_catigory()
            i = i + 1
        elif response == "4":
            rate_item()
            record_catigory()
            i = i + 1
        elif response == "5":
            rate_item()
            record_catigory()
            i = i + 1
        else:
            print("Please respond with a number between 1 and 5.")
    sleep(0.1)
    print("Great, you've completed the CoDa patterns inventory!")
    sleep(0.1)
    print("Some of these reflections may have brought up some feelings for you")
    sleep(0.1)
    print("Take a moment to check in with yourself")
    input()
    print("Did you identify any feelings that you would like to share?")
    response = input()
    if response in replies_yes:
        get_empathy()
    else:
        print("Would you like to review your inventory?")
        response = input()
        if response in replies_yes:
            print("I look forward to you writing that module")


# TO DO: Save following inside:
# set app.py to suggest an inventory if it has been over a week since the last entry.
# Create the option for additional comments for each pattern, which are saved to a pattern specific txt with timestamps followed by the comment

# Create new prayer module (seventh_sutra()) that grabs the 5s (or maybe just top 5 randomized whether or not there are more or less) list from the most recent inventory and rewords from do you, your to May I not, my. Could be upgraded with specific rewording in place of double negatives.
