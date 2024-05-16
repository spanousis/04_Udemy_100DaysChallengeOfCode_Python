"""
You are going to write a virtual coin toss program. 
It will randomly tell the user "Heads" or "Tails".

Important, the first letter shoudl be capitalised and spelt
exactly like in the example e.g. "Heads" or "Tails".

e.g. 1 means Heads 0 means Tails

Example
Heads

or

Tails

"""

import random

userInput = input("Head or Tails: ")
randomChoice = random.randint(0, 1)

# Heads is 0
# Tails is 1
userChoice = 0
if userInput == "Tails":
    userChoice = 1
    
if randomChoice == userChoice:
    print("You win!")
else:
    print("Your lose...")