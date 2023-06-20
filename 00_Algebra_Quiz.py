import random
import math


# Component 1
def yes_no(question):
    valid = False
    while not valid:
        response = input(question).lower()

        if response == "yes" or response == "y":
            return "yes"

        elif response == "no" or response == "n":
            return "no"

        else:
            print("Please answer yes / no")


def instructions():
    print("---------------------------")
    print("------ Instructions -------")
    print("---------------------------")
    print()
    print()
    print("Welcome to the algebra quiz")
    print()
    print("You can pick a difficulty by typing "
          "'easy' (e), 'medium' (m) or hard (h)")
    print()
    print("The amount of questions ask is also your choice you can pick any"
          "amount above 1")
    print()
    print("if you want infinite rounds you can press <enter> on your keyboard")
    print()

    return ""


# Asks user for what difficulty they want the questions to be
def difficulty_checker(question, valid_list, error):
    while True:
        response = input(question).lower()
        # Checks if response is in list of values
        # returns response
        for item in valid_list:
            # Accepts single letter or whole word as valid response
            if response == item[0] or response == item:
                response = item
                return response

        else:
            print(error)
        continue


def num_check(question, low=None, exit_code=None):
    while True:

        response = input(question)
        if response == exit_code:
            return response

        try:
            response = int(response)

            # Prints response based on situation
            if response < low:
                print(f"Please enter a number that is more"
                      f" than or equal to {low}")
                continue

            return response
        except ValueError:
            print("Please enter an integer")
            continue


def check_rounds():
    while True:
        response = input("How many questions: ")

        round_error = "Please enter an integer above 1 or <enter> for infinite rounds"

        if response != "":
            try:
                response = int(response)

                if response < 1:
                    print(round_error)
                    continue
            except ValueError:
                print(round_error)
                continue

        return response


# main routine

# Asks user if the want to see the instructions
show_instructions = yes_no("Would you like to see the instructions? ")
print()

if show_instructions == "yes":
    instructions()

# List of difficulties
difficulty_list = ["easy", "medium", "hard"]

# Asks user to select difficulty
difficulty = difficulty_checker("What difficulty would you like the questions: ",
                                difficulty_list, "Please pick easy (e), medium (m)"
                                                 ", or hard (h)")
print()

# Loops the quiz questions
play_again = "yes"
while play_again == "yes":

    # Generates random numbers for the quiz's questions
    num1 = random.randint(1, 20)
    num2 = random.randint(1, 20)
    x = random.randint(1, 10)
    num3 = num1 + x

    # Sets rounds played to zero and ask for number of rounds
    rounds_played = 0
    rounds = check_rounds()

    # Checks if difficulty is easy
    if difficulty == "easy":
        print("Easy Difficulty")
        print()

        # Generates values for question
        guesses = 3

        # Loops the same question until answer is correct or guess run out
        while guesses > 0:

            # Prints question for the user to see what they are trying to guess
            easy_question = f"{num1} + x = {num3}"
            print(easy_question)
            print()

            # Checks for users input
            guess = num_check("Find the value of X: ", 1, exit_code="xxx")

            # Checks if guess is correct or incorrect, lets user know
            if guess == x:
                print("Correct")
                break

            elif guess != x:
                guesses -= 1
                if guesses >= 1:
                    print(f"Incorrect you still have {guesses} guesses left!")

        # When guesses run out tell user and let them know what "X" was
        if guesses == 0:
            print(f"Sorry you ran out of guesses, 'x' was {x}")
            continue

    # Checks if difficulty is medium
    if difficulty == "medium":
        print("Medium Difficulty")
        print()

        guesses = 2

        # Loops the same question until answer is correct or guess run out
        while guesses > 0:

            # Prints question for the user to see what they are trying to guess
            medium_question = f"{num1} * x = {num3}"
            print(medium_question)
            print()

            # Checks for users input
            guess = num_check("Find the value of X: ", 1, "xxx")
            print()

            # Checks if guess is correct or incorrect, lets user know
            if guess == x:
                print("Correct")
                break

            elif guess != x:
                guesses -= 1
                if guesses >= 1:
                    print(f"Incorrect you still have {guesses} guesses left!")

        # When guesses run out tell user and let them know what "X" was
        if guesses == 0:
            print(f"Sorry you ran out of guesses, 'x' was {x}")
            continue

    # Checks if difficulty is hard
    if difficulty == "hard":
        print("Hard Difficulty")
        print()

        # Loops the same question until answer is correct or guess run out
        while True:

            # Prints question for the user to see what they are trying to guess
            hard_question = f"{num1} * x + {num2} = {num3}"
            print(hard_question)
            print()

            # Checks for users input
            guess = num_check("Answer: ", 1, "xxx")

            # Checks if guess is correct or incorrect, lets user know the "X" value
            if guess == x:
                print("Correct")
                break
            else:
                print(f"Sorry your answer was incorrect, 'x' was {x}!")
                break
