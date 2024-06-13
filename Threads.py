import threading
import time

def nums():
    for i in range(0,10):
        print("Numbers : ",i)
        time.sleep(1)

def alpha():
    for j in 'abcdefghijklmnopqrst':
        print("Alphabet : ",j)
        time.sleep(1)

t1 = threading.Thread(target=nums)
t1.start()
t2 = threading.Thread(target=alpha)
t2.start()
nums()
alpha()