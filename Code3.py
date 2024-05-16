"""

You are going to write a program that will selct a random name from a list of names. 
The person selected will have to pay for everybody's food bill.
Important: You are not allowed to use the choice() function.
Line 1 splits the string names_string into individual names and
puts them inside a List called names. For this to work, you must enter
all the names as names followed by comma then space.
e.g. name, name, name
NOTE: Don't worry about getting hold of the input(), we've done the work behind the scenes
to import everything.
HINT: Assumee that names looks like this:
input: x, y, z names = ["x", "y", "z"]
EXAMPLE INPUT:
Angela, Ben, Jenny, Michael, Chloe
NOTE: notice that there is a space between the comma and the next name
EXAMPLE OUTPUT:
Michael is going to buy the meal today!

"""

import random

names_string = input("Please type the names: ")
names = names_string.split(", ")
# names_string contains the input values provided
# The code above converts the input into an array seperating
# each name in the input by a comma and space.

listLen = len(names)
randomInt = random.randint(0, listLen)
print(f"{names[randomInt]} is going to buy the meal today!")