import module_two

print(__name__)
print(module_two.__name__)

def hello():
    print('Hello, world!')

if __name__ == '__main__':
    hello()