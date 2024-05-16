# ROCK - PAPER - SCISSORS

import random

choicesList = ["Rock", "Paper", "Scissors"]

while True:
    userChoice = input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.")
    userChoiceInt = int(userChoice)
    machineChoiceInt = random.randint(0, 2)

    result = userChoiceInt - machineChoiceInt
    print(f"You choose {choicesList[userChoiceInt]}")
    print(f"Machine chooses {choicesList[machineChoiceInt]}")

    if result == 0:
        print(f"It is a draw.")
    elif result == -1 or result == 2:
        print(f"You loose...")
    elif result == 1 or result == -2:
        print(f"You win!")

    if input("Would you like to play again? (yes or no): ") == "no":
        break
