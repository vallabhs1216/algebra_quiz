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


# List of difficulties
difficulty_list = ["easy", "medium", "hard"]

# Asks user to select difficulty
difficulty = difficulty_checker("What difficulty would you like the questions: ",
                                difficulty_list, "Please pick easy (e), medium (m)"
                                                 ", or hard (h)")
while True:
    # Tells us difficulty selected
    if difficulty == "easy":
        print("easy difficulty")

        # Generates values for question
        num1 = random.randint(1, 20)
        num2 = random.randint(1, 20)
        x = random.randint(1, 10)
        num3 = num1 + x
        guesses = 3

        # Loops the same question until answer is correct or guess run out
        while guesses > 0:

            # Prints question for the user to see what they are trying to guess
            easy_question = f"{num1} + x = {num3}"
            print(easy_question)

            # Checks for users input
            guess = num_check("Find the value of X: ", 1, "xxx")

            # Checks if guess is correct or incorrect, lets user know
            if guess == x:
                print("Correct")
                break

            elif guess != x:
                guesses -= 1
                if guesses >= 1:
                    print(f"Incorrect you still have {guesses} guesses left!")

        if guesses == 0:
            print(f"Sorry you ran out of guesses, 'x' was {x}")
            continue
