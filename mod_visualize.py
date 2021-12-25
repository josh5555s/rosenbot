import random
import datetime
from time import sleep
from list_feelings import *
from list_yes_or_no import *


def visualize():
    # Write timestamp of program launch
    vis_date = open("timestamps/visualization_date.txt", "a")
    vis_date.write(str(datetime.datetime.now()) + "\n")

    # set visualization duration
    duration_in_seconds = 60

    # Introduction text
    sleep(0.1)
    print("Okay, let's start with visualizing some feelings.")
    sleep(0.1)
    print("I will select a feeling at random,")
    sleep(0.1)
    print("then you hold how it feels in your body")
    sleep(0.1)
    print(
        f"I will let you know when the time is up after {duration_in_seconds} seconds"
    )
    sleep(0.1)
    print("Then we can move to the next one.")
    sleep(0.1)
    print(
        "Would you like to practice with only positive feelings, or include negitive ones as well?"
    )
    sleep(0.1)
    print("Reply 'p' for positive only or 'b' for both.")
    pick = input()
    print("Sounds good. Let me know when you are ready")
    input()
    sleep(0.1)
    print("Okay, let's begin, your first feeling is...")
    sleep(1)

    # set visualization duration
    duration_in_seconds = 60
    i = 0
    shuffled_feelings = ""
    if pick == "p":
        shuffled_feelings = feelings_positive
    elif pick == "b":
        shuffled_feelings = feelings_positive + feelings_negative
    random.shuffle(shuffled_feelings)
    while i < 30:
        print(str(shuffled_feelings[i].capitalize()))
        sleep(duration_in_seconds)
        print("Okay, time is up.")
        if i == 4:
            print("That makes five in a row, great work!")
        if i == 9:
            print(
                "That makes ten in a row, god damn! Maybe think of giving yourself a break?"
            )
        sleep(0.5)
        # TO DO - Was there any specific imagery that helped you visualize this feeling? (record it to txt for use later)
        print("Ready for another one?")

        ready = input()
        if ready in replies_yes:
            sleep(0.7)
            print("Great, here is the next one...")
            sleep(1)
            i += 1
        else:
            i = 30
    print("Congrats, that was some solid visualization practice!")


# TO DO:
# Add followup questions after the visualization period, including:
# 1 to 5: how intense was the cultivated emotion?
# if previous response was 4 or 5: what imagery helped facilite the emotion?
# Similar to inventory filesystem, create folder with date for each visualization session.
# save all feelings into txt titled 1 through 5.
# Save effective imagery (with entry dates) to feeling txt files in the parent dir.
