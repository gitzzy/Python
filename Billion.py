import time

start_time = time.time()
print("Starting")
for i in range(0,1000000001):
    if(i==1000000000):
        print("Hi")
        end_time = time.time()
        execution_time = end_time - start_time
        print(f"Execution Time: {execution_time} seconds")