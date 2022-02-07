# Derive from more than one class

class Human:
    def be_human(self):
        print("I'm only human after all")

class Man:
    def man(self):
        print("Be strong")

class Male(Human, Man):
    def male(self):
        print("Male Things")

male = Male()
male.be_human()
male.man()
male.male()