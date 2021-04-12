from multiprocessing import Pool
from multiprocessing.managers import BaseManager


class QueueManager(BaseManager):
    pass


QueueManager.register('out_queue')
m = QueueManager(address=('192.168.100.13', 8080), authkey=b'abracadabra')
m.connect()
queue2 = m.out_queue()


tasks_done = []
while(not queue2.empty()):
    l = queue2.get()
    tasks_done.append(l)

print(tasks_done)
