while True:
    name = input("Name:")
    print(name)
    if name == 'q':
        break

phone = '123-456-7890'

for i in phone:

    if i == '-':
        pass
    else:
        print(i)