from multiprocessing import Pool
from multiprocessing.managers import BaseManager


class QueueManager(BaseManager):
    pass


QueueManager.register('get_queue')
QueueManager.register('out_queue')
m = QueueManager(address=('192.168.100.13', 8080), authkey=b'abracadabra')
m.connect()
queue = m.get_queue()
queue2 = m.out_queue()

tasks = []


def mnoz(task):
    id = task[0]
    A = task[1]
    X = task[2]

    ncols = len(A)
    s = 0
    for c in range(ncols):
        s += A[c] * X[c][0]

    queue2.put((id, s))
    # print((id, s))


while(not queue.empty()):
    l = queue.get()
    tasks.append(l)
# print(tasks)
if __name__ == '__main__':
    with Pool(32) as p:
        p.map(mnoz, tasks)
