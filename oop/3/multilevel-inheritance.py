class Organism:
    alive = True

class Animal:

    def eat(self):
        print("This animal is eating")

class Dog(Animal, Organism):

    def bark(self):
        print("This animal is barking")

class Cat(Animal, Organism):

    def meow(self):
        print("This animal is meowing")

dog = Dog()
dog.eat()
print(dog.alive)

cat = Cat()
cat.eat()
cat.meow()
print(cat.alive)

