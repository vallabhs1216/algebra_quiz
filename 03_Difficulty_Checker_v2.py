# Component 3 - Asks user for what difficulty they want the questions to be
def difficulty_checker(question):
    while True:
        response = input(question).lower()
        if response == "easy" or response == "e":
            return "easy"

        elif response == "medium" or response == "m":
            return "medium"

        elif response == "hard" or response == "h":
            return "hard"
        else:
            print("Please pick easy (e), medium (m), or hard (h): ")


# Asks for difficulty
difficulty = difficulty_checker("What difficulty would you like the questions: ")

# Tells us difficulty selected
if difficulty == "easy":
    print("Easy difficulty")

elif difficulty == "medium":
    print("Medium difficulty")

elif difficulty == "hard":
    print("Hard difficulty")
