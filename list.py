foods = ["pizza", "hamburger", "chicken", "steak", "salad", "apple", "banana", ]

foods[0] = "new food"

print(foods)

foods.append("ice cream")
foods.remove("chicken")
foods.pop()
foods.insert(0, "cake")
foods.sort()
foods.clear()

for food in foods:
    print(food)