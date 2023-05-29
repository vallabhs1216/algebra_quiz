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


# List of difficulties
difficulty_list = ["easy", "medium", "hard"]

# Asks user to select difficulty
difficulty = difficulty_checker("What difficulty would you like the questions: ",
                                difficulty_list, "Please pick easy (e), medium (m)"
                                                 ", or hard (h)")
x = random.randint(1, 10)
num1 = random.randint(1, 50)
num2 = random.randint(1,50)
# Tells us difficulty selected
if difficulty == "easy":
    print("Easy difficulty")

    easy_question = f"{num2} * {x} + {num1}"
    print(easy_question)
    answer = num2 * x + num1

