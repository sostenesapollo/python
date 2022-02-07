# *args will pack all arguments into a [tuple]

def add(*stuff):
    sum = 0 
    stuff = list(stuff)
    for i in stuff:
        sum += i
    return  sum

print(add(1,1,5))

def join_terms(*terms):
    s = " "
    for i in terms:
        s += ' {}'.format(i)
    return s

print(join_terms("hello", "world,", "how", "are", "you"))