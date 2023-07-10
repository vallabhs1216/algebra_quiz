import random


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
    print("Welcome to the algebra quiz")
    print()
    print("You can pick a difficulty by typing 'easy' (e), 'medium' (m) or 'hard' (h)")
    print()
    print("The number of questions asked is also your choice; you can pick any amount above 1")
    print()
    print("If you want infinite rounds, you can press <enter> on your keyboard")
    print()


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

        print(error)


def num_check(question, low=None, exit_code=None):
    while True:
        response = input(question)
        if response == exit_code:
            return response

        try:
            response = int(response)

            # Prints response based on situation
            if response < low:
                print(f"Please enter a number that is more than or equal to {low}")
                continue

            return response
        except ValueError:
            print("Please enter an integer")


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

# Asks the user if they want to see the instructions
show_instructions = yes_no("Would you like to see the instructions? ")
print()

if show_instructions == "yes":
    instructions()

# List of difficulties
difficulty_list = ["easy", "medium", "hard"]

# Asks the user to select the difficulty
difficulty = difficulty_checker("What difficulty would you like the questions (easy, medium, or hard): ",
                                difficulty_list, "Please pick 'easy' (e), 'medium' (m), or 'hard' (h)")
print()

# Loops the quiz questions
try_again = "yes"

# Sets rounds and rounds play to be equal
rounds = 1
rounds_played = rounds

# Text results for testing
result_picker = random.randint(1,2)
if result_picker == 1:
    test_results = ["correct", "correct", "incorrect", "correct", "incorrect"]
else:
    test_results = []

# If the user enters the exit code, ask if they would like to play again
if try_again == "yes" or try_again == "y":
    if rounds_played == rounds:
        print()
        if len(test_results) >= 1:
            game_history = input("Do you want to see your results? ")

            if game_history == "yes" or game_history == "y":
                print()
                print("******** Test results ********")
                for result in test_results:
                    print(result)

        try_again = input("Would you like to try again? ")



print()
print("Thanks for playing")
