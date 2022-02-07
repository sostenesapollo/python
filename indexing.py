#indexing operator [] = gives access to a sequence's element (str, list, luples)

name = "test Text !"

if(name[0].islower()):
    name = name.capitalize()

print(name)

first_name = name[0:4].upper()
last_name = name[5:].capitalize()
last_char = name[-1]

print(first_name,'-', last_name, '>',  last_char)