
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


# Main routine goes here


rounds_played = 0

choose_instruction = f"Find the value of 'X' "

# Ask user for # of rounds or <enter> for infinite rounds
rounds = check_rounds()

end_game = "no"
while end_game == "no":

    # Rounds Heading
    print()
    if rounds == "":
        heading = f"Continuous Mode: Round {rounds_played + 1}"
    else:
        heading = f"Round {rounds_played + 1} of " \
                  f"{rounds}"
    print(heading)
    choose = input(f'{choose_instruction}("xxx" to quit) ')

    if choose == "xxx":
        break

    rounds_played += 1
    # End game if round limit is reached
    if rounds_played == rounds:
        break

print("Thanks for playing")
