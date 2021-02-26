from collections import deque
import time

start_time = time.process_time()
deque_list = deque()
# Stack
for i in range(10000):
    for j in range(10000):
        deque_list.append(j)
        deque_list.pop()
print(time.process_time() - start_time, "seconds")
