# Derive from more than one class

class Human:
    def man(self):
        print("Method 1")

class Man(Human):
    def man(self):
        print("Method 2")

human = Man()
human.man()