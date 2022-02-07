import time,threading

def a():
    print('run a')
    time.sleep(2)
    print('a')

def b():
    print('run b')
    time.sleep(3)
    print('b')

x = threading.Thread(target=a, args=())
x.start()
y = threading.Thread(target=b, args=())
y.start()

x.join()
y.join()

print('threads:', threading.active_count())
print(threading.enumerate())
print(time.perf_counter())
