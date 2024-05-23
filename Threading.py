import threading
import time

def Start():
    for i in range(0,10):
        print(i)
        time.sleep(1)

def Reverse():
    for i in range(10,0,-1):
        print(i)
        time.sleep(1)

t1 = threading.Thread(target=Start)
t1.start()
t2 = threading.Thread(target=Reverse)
t2.start()
t1.join()
print("End")