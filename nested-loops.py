rows = int(input('How many rows? '))
columns = int(input('How many columns? '))
symbol = input('Symbol to use:')

for i in range(rows):
    for i in range(columns):
        print(symbol, end='')
    print()

