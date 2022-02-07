from multiprocessing import Process
from time import sleep


def func1(j1):
    rocket = j1
    print('start func1')
    while rocket < 10:
        rocket += 1
        sleep(5)
        print(rocket, " -r1")
    print('end func1')


def func2(j2):
    rocket = j2
    print('start func2')
    while rocket < 30:
        rocket += 1
        sleep(2)
        print(rocket, " -r2")
    print('end func2')


if __name__ == '__main__':
    p1 = Process(target=func1, args=(0,))
    p1.start()
    p2 = Process(target=func2, args=(10,))
    p2.start()