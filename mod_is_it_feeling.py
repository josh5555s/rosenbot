import random
import time
import list_why_faux
from time import sleep
from list_feelings import *

# from feeling_responses import *
from list_yes_or_no import *


def is_it_feeling():
    print(
        "Okay, in this game I will say either a feeling or a faux feeling and you will say which it is."
    )
    sleep(0.1)
    print(
        "The game will end after one minute and you will see your score and relevent stats."
    )
    sleep(0.1)
    print(
        "You gain a point for every correct answer and lose a point for every incorrect answer."
    )
    sleep(0.1)
    print("Reply 't' for true for 'f' for faux. Let me know when you are ready")
    input()
    sleep(0.1)
    print("Okay, let's begin...")
    sleep(1)

    shuffled_feelings = (
        feelings_positive
        + feelings_negative
        + faux_feelings_positive
        + faux_feelings_negative
    )

    duration_in_seconds = 60
    while True:
        random.shuffle(shuffled_feelings)
        # set timer
        t_end = time.time() + duration_in_seconds
        i = 0  # to cycle through feelings array
        correct = 0
        incorrect = 0
        missed = ""
        while time.time() < t_end:
            print(shuffled_feelings[i])
            response = input()
            print("")
            if response == "t" and shuffled_feelings[i] in feelings_all:
                correct = correct + 1
                # print("Correct: 't' and in feelings_all \n")
            elif response == "f" and shuffled_feelings[i] not in feelings_all:
                correct = correct + 1
                # print("Correct: 'f' and in faux_feelings_all \n")
            elif response == "t" and shuffled_feelings[i] not in feelings_all:
                incorrect = incorrect + 1
                missed += f"| {shuffled_feelings[i]} "
                # print("Incorrect: 'f' and not in feelings_all \n")
            elif response == "f" and shuffled_feelings[i] in feelings_all:
                incorrect = incorrect + 1
                missed += f"| {shuffled_feelings[i]} "
                # print("Incorrect: 'f' and in feelings_all \n")
            else:
                print("Type either 't' for a true feeling for 'f' for a faux feeling")
            i = i + 1

        print("=------------------------=")
        print("Time is up!")
        score = correct - incorrect
        sleep(0.1)
        print(f"Score: {str(score)}")
        sleep(0.1)
        print(f"Correct: {str(correct)}")
        sleep(0.1)
        print(f"Incorrect: {str(incorrect)}")
        sleep(0.1)
        print(f"Missed: {missed}")
        sleep(0.1)
        print(f"Response/Second: {(correct + incorrect) / duration_in_seconds}")
        sleep(0.1)
        print("=------------------------=")
        print("Play again? Or, lookup a faux feeling for an explination.")
        response = input()
        if response in replies_yes:
            print("Okay, let's begin...")
            sleep(1)
        elif response in replies_no:
            print("'n' fired'")
            break
        elif response in faux_feelings_all:
            print("why_faux() fired")
            break
        else:
            print("else fired")
            break
