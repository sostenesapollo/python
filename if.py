age = int(input('How old are you? '))

if age >= 18:
    print('adult')
elif age < 0:
    print('not born yet')
else:
    print('child')