import random


def easy_question():
    num1 = random.randint(1, 10)
    x = random.randint(1, 10)
    operator = random.choice(["+", "-"])
    if operator == "+":
        num3 = num1 + x
    else:
        num3 = num1 - x
    question = f"{num1} {operator} {x} = {num3}"
    return question, num1


def medium_question():
    num1 = random.randint(1, 10)
    x = random.randint(1, 10)
    operator = random.choice(["*", "/"])
    if operator == "*":
        num3 = num1 * x
    else:
        num3 = num1 / x
    question = f"{num1} {operator} {x} = {num3}"
    return question, num1


def hard_question():
    num1 = random.randint(1, 10)
    x = random.randint(1, 10)
    num3 = random.randint(1, 10)
    operator = random.choice(["x", "/"])
    if operator == "x":
        num4 = num1 * x + num3
    else:
        num4 = num1 / x + num3

    question = f"{num1} {operator} {x} {operator} {num3} = {num4}"
    return question, x


def answer_checker(attempt, x, attempts_left):
    if attempt == x:
        print("Correct")
        return "correct"
    elif attempt == "xxx":
        return "exit"
    else:
        attempts_left -= 1
        if attempts_left > 0:
            print(f"Incorrect, you still have {attempts_left} attempt(s) left!")
        else:
            print(f"Sorry, you ran out of attempts. The correct answer was {x}")
        return "incorrect"


def play_quiz(difficulty):
    if difficulty == "easy":
        generate_question = easy_question
        attempts_allowed = 3
    elif difficulty == "medium":
        generate_question = medium_question
        attempts_allowed = 2
    elif difficulty == "hard":
        generate_question = hard_question
        attempts_allowed = 1
    else:
        print("Invalid difficulty level.")
        return

    print(f"{difficulty.capitalize()} Difficulty\n")

    rounds_played = 0
    test_results = []

    while True:
        rounds_played += 1
        question, x = generate_question()

        print(f"Question {rounds_played}")
        print(question)
        print()

        attempts_left = attempts_allowed
        already_attempted = []

        while attempts_left > 0:
            attempt = input("Find the value of X: ")
            result = answer_checker(attempt, x, attempts_left)
            if attempt == "correct":
                test_results.append("correct")
                break
            elif result == "exit":
                rounds_played -= 1
                break
            else:
                already_attempted.append(attempt)
                attempts_left -= 1
                if attempts_left > 0:
                    print(
                        f"You already tried that number! Please try again. You still have {attempts_left} attempt(s) "
                        f"left")
                else:
                    test_results.append("incorrect")
                    break

        if rounds_played >= 1:
            try_again = input("Would you like to play again? (yes/no): ")
            if try_again.lower() != "yes":
                break

    print()
    print("Thanks for playing!")


play_quiz("easy")  # Start the quiz with easy difficulty
