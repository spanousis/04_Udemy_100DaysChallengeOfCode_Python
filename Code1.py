import random
import myModule

c = random.randrange(100, 200)
randomInteger = random.randint(1, 10)
print(randomInteger)
print(c)

print(myModule.pi)

randomFloat = random.random()
print(randomFloat)

randomFloat_ = randomInteger + randomFloat
print(randomFloat_)

loveScore = random.randint(1, 100)
print(f"Your love score is {loveScore}")

# LISTS
statesOfAmerica = [
    "Delaware", 
    "Pennsylvania", 
    "New Jersey", 
    "Georgia", 
    "Connecticut", 
    "Massachusetts",
    "Maryland", 
    "South Carolina", 
    "New Hampshire",
    "Virginia", 
    "New York", 
    "North Carolina",
    "Rhode Island", 
    "Vermont", 
    "Kentucky", 
    "Tennessee", 
    "Ohio", 
    "Louisiana", 
    "Indiana", 
    "Mississippi", 
    "Illinois", 
    "Alabama", 
    "Maine", 
    "Missouri", 
    "Arkansas",
    "Michigan", 
    "Florida",
    "Texas", 
    "Iowa", 
    "Wisconsin",
    "California", 
    "Minnesota", 
    "Oregon", 
    "Kansas",
    "West Virginia", 
    "Nevada", 
    "Nebraska", 
    "Colorado",
    "North Dakota", 
    "South Dakota", 
    "Montana",
    "Washington", 
    "Idaho", 
    "Wyoming", 
    "Utah", 
    "Oklahoma",
    "New Mexico", 
    "Arizona", 
    "Alaska", 
    "Hawaii"
]

print(statesOfAmerica[0])
state = statesOfAmerica[-1]
print(state)

"""
statesOfAmerica[1] = "Sotiris"
statesOfAmerica.append("Panousis")
statesOfAmerica.extend(["SotirisLand", "Jack Bauer Land"])
"""

print(statesOfAmerica)

fruits = [
    "Strawberries", 
    "Nectarines", 
    "Apples", 
    "Grapes",
    "Peaches",
    "Cherries",
    "Pears"
]

vegetables = [
    "Spinach",
    "Kale",
    "Tomatoes",
    "Celery",
    "Potatoes"
]

dirty_dozen = [fruits, vegetables]
print(dirty_dozen)