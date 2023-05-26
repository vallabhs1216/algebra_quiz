# Component 3 - Asks user for what difficulty they want the questions to be
def difficulty_checker(question, valid_list, error):
    while True:
        response = input(question).lower()
        # Checks if response is in list of values
        # returns appropriate response
        for item in valid_list:
            if response == item[0] or response == item:
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

# Tells us difficulty selected
if difficulty == "easy":
    print("Easy difficulty")

elif difficulty == "medium":
    print("Medium difficulty")

elif difficulty == "hard":
    print("Hard difficulty")
