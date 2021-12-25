

user_response_feeling = "PLACEHOLDER"


def feeling_responses():
    bot_responses_to_positive_user_feeling = [
        "So you are feeling " + user_response_feeling + " huh? That is good to hear.",
        user_response_feeling.capitalize() + "! Well that is nice to hear.",
        "Good to hear that you are feeling " + user_response_feeling + ".",
    ]

    bot_responses_to_negitive_user_feeling = [
        "You are feeling " + user_response_feeling + " huh? I'm sorry to hear that.",
        user_response_feeling + "? Well that sucks.",
        "I'm sorry to hear that you are feeling " + user_response_feeling + ".",
    ]
