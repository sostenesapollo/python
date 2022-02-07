import time, threading, os

def timer():
    count = 0
    while True:
        time.sleep(1)
        count += 1
        os.mkdir(str(count))
        print(str(count))

x = threading.Thread(target=timer, daemon=True)
x.start()

input('Press enter to exit\n')