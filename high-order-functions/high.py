def f1(text):
    return text+' f1 '

def f2(func):
    return func('f2')

print(f2(f1))