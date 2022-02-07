# Returns a temporary object of a parent class

class Rectangle:

    def __init__(self, length, width):
        self.length = length
        self.width = width

class Square(Rectangle):
    
    def __init__(self, length):
        super().__init__(length, length)
    
    def area(self):
        return self.length * self.width

class Cube(Rectangle):
    # This super method calls the __init__ method of the parent class
    # and passes the arguments to it.
    def __init__(self, length, width, height):
        super().__init__(length, width)
        self.height = height
    
    def volume(self):
        return self.length * self.width * self.length

cube = Cube(2,2,2)
print(cube.volume())