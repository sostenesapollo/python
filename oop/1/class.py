from car import Car

honda = Car('Honda', 'Civic', 2017, 'red')

print(honda.make, honda.model, honda.color, honda.year, honda.wheels)

Car.wheels = 2
moto = Car('Honda', 'POP', 2015, 'blue')
print(moto.make, moto.model, moto.color, moto.year, moto.wheels)

honda.drive()
honda.stop()