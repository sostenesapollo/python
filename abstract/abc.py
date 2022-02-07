from abc import ABC, abstractmethod

class Vehicle(ABC):

    @abstractmethod
    def go(self):
        pass

class Car:
    def go(self):
        print("Driving a car")

class Motorcycle:
    def go(self):
        print("Ride motorcycle")

# With abstract method this Will Not be allowed:
# vehicle = Vehicle()

Car().go()
Motorcycle().go()