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
while try_again == "yes" or try_again == "y":

    # Sets rounds played to zero and asks for the number of rounds
    rounds_played = 0
    rounds = check_rounds()
    test_results = []
    results = ""
    # Checks if mode is regular and prints short instruction
    start = ""
    mode = "regular"
    choose_instruction = "Pick a number"

    # Checks if mode is infinite
    if rounds == "":
        mode = "infinite"
        rounds = 5

    while rounds_played < rounds:

        # Rounds Heading - Displays if the user has chosen infinite or normal mode
        # Along with how many rounds have been played.
        print()

        if mode == "infinite":
            heading = f"Continuous Mode: Question {rounds_played + 1}"
            rounds += 1
        else:
            heading = f"Question {rounds_played + 1} of {rounds}"
        print(heading)
        print(f"{choose_instruction} or 'xxx' to end ")

        rounds_played += 1

        # Checks if difficulty is easy
        if difficulty == "easy":
            # Generates random numbers for the quiz's questions
            num1 = random.randint(1, 20)
            x = random.randint(1, 10)
            num3 = num1 + x

            print("Easy Difficulty")
            print()

            # Calculates guessed allowed and guesses left
            attempts_allowed = 3
            attempts_left = attempts_allowed
            # Holds a list of already guessed values
            already_attempted = []
            scores = []
            result = ""
            # Loops the same question until the answer is correct or the guesses run out
            while attempts_left >= 1:

                # Prints the question for the user to see what they are trying to guess
                easy_question = f"{num1} + x = {num3}"
                print(easy_question)
                print()

                # Checks the user's input
                attempt = num_check("Find the value of X: ", 1, "xxx")

                # Checks if the guess is correct or incorrect and lets the user know
                if attempt == x:
                    print("Correct")
                    result = "correct"
                    break

                if attempt == "xxx":
                    rounds_played = rounds
                    break

                if attempt in already_attempted:
                    print(
                        f"You already tried that number! "
                        f"Please try again. You still have "
                        f"{attempts_left} attempts left")
                    continue
                attempts_left -= 1
                already_attempted.append(attempt)

                if attempts_left >= 1:
                    print(f"Incorrect, you still have {attempts_left} guesses left!")

            # When the guesses run out, tell the user and let them know what "X" was
            if attempts_left == 0:
                print(f"Sorry, you ran out of attempts. 'x' was {x}")
                result = "incorrect"

            # gets results for game history
            tries_taken = ""
            if result == "correct":
                tries_taken = f"| it took {3 - attempts_left + 1} attempt(s)"
            feedback = f"{result} {tries_taken}"
            test_results.append(feedback)

        # Checks if difficulty is medium
        if difficulty == "medium":
            # Generates random numbers for the quiz's questions
            num1 = random.randint(1, 20)
            x = random.randint(1, 10)
            num3 = num1 * x

            print("Medium Difficulty")
            print()

            # Calculates guessed allowed and guesses left
            attempts_allowed = 2
            attempts_left = attempts_allowed
            # Holds a list of already guessed values
            already_attempted = []
            result = ""
            # Loops the same question until the answer is correct or the guesses run out
            while attempts_left > 0:

                # Prints the question for the user to see what they are trying to guess
                medium_question = f"{num1} * x = {num3}"
                print(medium_question)
                print()

                # Checks the user's input
                attempt = num_check("Find the value of X: ", 1, "xxx")
                print()

                # Checks if the guess is correct or incorrect and lets the user know

                if attempt == x:
                    print("Correct")
                    result = "correct"
                    break

                if attempt == "xxx":
                    rounds_played = rounds
                    break

                if attempt in already_attempted:
                    print(
                        f"You already tried that number! "
                        f"Please try again. You still have "
                        f"{attempts_left} attempts left")
                    continue
                attempts_left -= 1
                already_attempted.append(attempt)

                if attempts_left >= 1:
                    print(f"Incorrect, you still have {attempts_left} attempts left!")

            # When the guesses run out, tell the user and let them know what "X" was
            if attempts_left == 0:
                print(f"Sorry, you ran out of tries. 'x' was {x}")
                result = "incorrect"

            # gets results for game history
            tries_taken = ""
            if result == "correct":
                tries_taken = f"| it took {2 - attempts_left + 1} attempt(s)"

            feedback = f"{result} {tries_taken}"
            test_results.append(feedback)

        # Checks if difficulty is hard
        if difficulty == "hard":
            # Generates random numbers for the quiz's questions
            num1 = random.randint(1, 20)
            x = random.randint(1, 10)
            num2 = random.randint(1, 20)
            num3 = num1 * x + num2

            attempts_allowed = 1
            attempts_left = attempts_allowed
            result = ""

            print("Hard Difficulty")
            print()

            while True:
                # Prints the question for the user to see what they are trying to guess
                hard_question = f"{num1} * x + {num2} = {num3}"
                print(hard_question)
                print()

                # Checks the user's input
                attempt = num_check("Answer: ", 1, "xxx")

                # Checks if the attempt is correct or incorrect and lets the user know the "X" value
                if attempt == x:
                    print("Correct")
                    result = "correct"
                    break

                if attempt == "xxx":
                    rounds_played = rounds
                    break

                else:
                    print(f"You didn't get it. 'x' was {x}")
                    result = "incorrect"
                    break

                # gets results for game history
            feedback = f"{result}"
            test_results.append(feedback)

        # If the user enters the exit code, ask if they would like to play again
        if rounds_played == rounds:
            print()

            if len(test_results) > 1:
                game_history = input("Do you want to see your results? ")

                if game_history == "yes" or game_history == "y":

                    print()
                    print("******** Test results ********")
                    for results in test_results:
                        print(results)

            try_again = input("Would you like to try again? ")

        if try_again == "no" or try_again == "n":
            break

print()
print("Thanks for playing")
