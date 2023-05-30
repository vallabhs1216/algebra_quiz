
guesses_allowed = 3
x = 6
# List for already guessed integers
already_guessed = []
guesses_left = guesses_allowed
num_won = 0

guess = ""

while guess != x and guesses_left >= 1:

    guess = int(input("Guess: "))

    # Checks for duplicate guess
    if guess in already_guessed:
        print("You already guessed that number! Please try again"
              f" You still have {guesses_left} guesses left")
        continue

    guesses_left -= 1
    already_guessed.append(guess)

    if guesses_left >= 1:

        if guess < x:
            print(f"Too low, try guessing a higher number. \t|\t "
                  f"Guesses left: {guesses_left}")
        elif guess > x:
            print("Too high, try guessing a lower number. \t|\t"
                  f"Guesses left: {guesses_left}")
        else:
            if guess < x:
                print("Too low!")
            elif guess > x:
                print("Too high!")
if guess == x:
    if guesses_left == guesses_allowed - 1:
        print("Congratulations you got it on your first guess!")
    else:
        print("Well done you got the secret number correct")
if guesses_left < 1:
    print("Sorry you didn't get it in the amount of guesses given.")
