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
