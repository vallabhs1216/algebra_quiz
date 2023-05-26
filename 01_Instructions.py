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
    print("if you want infinite rounds you can press <enter> on your keyboard")

    return ""


# main routine


show_instructions = yes_no("Would you like to see the instructions? ")
if show_instructions == "yes":
    instructions()
