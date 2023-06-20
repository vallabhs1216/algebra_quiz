import math
import random


# Asks user for what difficulty they want the questions to be
def difficulty_checker(question, valid_list, error):
    while True:
        response = input(question).lower()
        # Checks if response is in list of values
        # returns appropriate response
        for item in valid_list:
            # Accepts single letter or whole word as valid response
            if response == item[0] or response == item:
                response = item
                return response

        else:
            print(error)
        continue


def num_check(question, low=None, exit_code=None):
    situation = ""

    # Checks for situation
    if low is not None:
        situation = "low only"

    while True:

        response = input(question)
        if response == exit_code:
            return response

        try:
            response = int(response)

            # Prints response based on situation
            if situation == "low only":
                if response < low:
                    print(f"Please enter a number that is more"
                          f" than or equal to {low}")
                    continue

            return response
        except ValueError:
            print("Please enter an integer")
            continue


# List of difficulties
difficulty_list = ["easy", "medium", "hard"]

# Asks user to select difficulty
difficulty = difficulty_checker("What difficulty would you like the questions: ",
                                difficulty_list, "Please pick easy (e), medium (m)"
                                                 ", or hard (h)")
while True:
    # Tells us difficulty selected
    if difficulty == "easy":
        print("Easy difficulty")
        guesses = 3

        # Generates values for question
        x = random.randint(1, 10)
        num1 = random.randint(1, 20)
        num2 = random.randint(1, 20)
        num3 = num1 + x

        while guesses >= 1:

            easy_question = f"{num1} + x = {num3}"
            print(easy_question)
            guess = num_check("Answer: ", 1, "xxx")
            if guess == x:
                print("Correct")
                continue
            elif guess != x:
                guesses -= 1
                print(f"Incorrect, you still have {guesses} tries left")

