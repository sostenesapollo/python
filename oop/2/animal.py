# inheritance

class Animal:
    alive = True

    def eat(self):
        print("This animal is eating")

    def sleep(self):
        print("This animal is sleeping")

class Rabbit(Animal):

    def jump(self):
        print("This animal is jumping")

class Fish(Animal):

    def swim(self):
        print("This animal is swimming")

rabbit = Rabbit()
fish = Fish()

print(rabbit.alive)

rabbit.eat()
rabbit.sleep()
rabbit.eat()

rabbit.jump()