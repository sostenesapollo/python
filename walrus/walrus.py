# Walrus operator

from bcrypt import hashpw


happy = True
print(happy := False)
print(happy)


foods = list()
while food := input("What food you like ?") != "quit":
    foods.append(food)