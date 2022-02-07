class Car:
    
    def brake(self):
        print("Car breaking")
        return self

    def accelerate(self):
        print("Car accelerating")

car = Car()
car.brake().accelerate()
