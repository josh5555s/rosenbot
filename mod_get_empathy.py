import random
from time import sleep
from list_feelings import *

# from feeling_responses import *
from list_needs import *
from list_yes_or_no import *


def get_empathy():
    while True:
        print("How are you feeling? You can reply 'g' if you'd like me to guess.")

        user_response_feeling = input()  # make lower case
        if user_response_feeling == "g":
            shuffled_feelings = feelings_positive + feelings_negative
            random.shuffle(shuffled_feelings)
            i = 0  # to cycle through feelings array
            while True:
                print(f"Are you feeling {shuffled_feelings[i]}?")
                response = input()
                if response in replies_yes:
                    user_response_feeling = shuffled_feelings[i]
                    break
                elif response in replies_no:
                    i = i + 1
                    continue  # to loop
                else:
                    "I didn't understand that, update me if I should."

        sleep(0.1)

        bot_responses_to_positive_user_feeling = [
            f"So you are feeling {user_response_feeling} huh? That is good to hear.",
            f"{user_response_feeling.capitalize()}! Well that is nice to hear.",
            f"Good to hear that you are feeling {user_response_feeling}.",
        ]

        bot_responses_to_negitive_user_feeling = [
            f"You are feeling {user_response_feeling} huh? I'm sorry to hear that.",
            f"{user_response_feeling.capitalize()}? Well that sucks!",
            f"I'm sorry to hear that you are feeling {user_response_feeling}.",
        ]

        # Check if feeling is positive or negative, check if need is true, respond accordingly
        if str(user_response_feeling) in (feelings_positive):
            print(str(random.choice(bot_responses_to_positive_user_feeling)))
            print(
                f"What needs of yours do you think are being met that make you feel {user_response_feeling}?"
            )
            # need_check
            user_response_needs = input()
            if user_response_needs in needs_all:
                print(
                    f"I'm hearing that you are feeling {user_response_feeling} because your need for {user_response_needs} is being met. Is that right?"
                )
                reflection = input()
                if reflection in replies_yes:
                    print(
                        f"Thank you for sharing that with me. Seeing you feeling {user_response_feeling} makes me feel {user_response_feeling}."
                    )
                else:
                    print(
                        "I'm sorry I misunderstood what you were saying. Let's try again."
                    )
            else:
                print(
                    "I'm not sure if that is an actual need.  Maybe it is more of a desire? Otherwise, maybe it needs to be added to my list. Could you double check and get back to me on that?"
                )

        # if user response is a negative feeling
        elif str(user_response_feeling) in (feelings_negative):
            print(f"{random.choice(bot_responses_to_negitive_user_feeling)}")
            sleep(0.1)
            print(
                f"What needs of yours do you think are not being met, making you feel {user_response_feeling}?"
            )

            # need_check
            user_response_needs = input()
            if user_response_needs in needs_all:
                print(
                    f"I'm hearing that you are feeling {user_response_feeling} because your need for {user_response_needs} is not being met.  Is that right?"
                )
                reflection = input()
                if reflection in replies_yes:
                    print("Thank you for sharing that with me.")
                    sleep(0.1)
                    print(
                        f"When you risk the vulnerability of me seeing you feeling {user_response_feeling}, it gives me the gift of feeling {random.choice(feelings_compassionate)} towards you."
                    )
                else:
                    print(
                        "I'm sorry I misunderstood what you were saying. Let's try again."
                    )
            else:
                print(
                    "I'm not sure if that is an actual need.  Maybe it is more of a desire? Otherwise, maybe it needs to be added to my list. Could you double check and get back to me on that?"
                )
        # if user response is a faux feeling
        elif str(user_response_feeling) in (faux_feelings_positive) or str(
            user_response_feeling
        ) in (faux_feelings_negative):
            print(
                f"'{user_response_feeling.capitalize()}' is not actually a feeling, but a judgement about yourself or your situation.  This is known as a faux feeling."
            )
            sleep(0.1)
            print(
                "One way to think about the difference is that a feeling is in your body, and a faux feeling actually requires a story in your head."
            )
            sleep(0.1)
            print(
                "I'd like to give you some empathy, but we will need to work with a real feeling in order to do that."
            )
        else:
            print(
                "ERROR: You typed something that is not included in the feeling lists. Check for misspelling, otherwise, look into expanding the feeling list."
            )

        # TO DO: Ask what event met that need, and write that to a need specific txt with timestamp.
        sleep(1)
        print("Would you like to get some more empathy?")
        response = input()
        if response in replies_no:
            break
