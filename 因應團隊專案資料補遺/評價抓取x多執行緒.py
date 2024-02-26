import threading
from queue import Queue

def job(data):
    for i in range(len(data)):
        data[i]= data[i] ** 2
    return data

q = Queue()

q.put(10)
q.put(11)
q.put(12)
q.put(13)

print(q.qsize())
for i in range(q.qsize()):
    print(q.get())