import json
from multiprocessing.managers import BaseManager
import sys


class QueueManager(BaseManager):
    pass


def read(fname):
    f = open(fname, "r")
    nr = int(f.readline())
    nc = int(f.readline())

    A = [[0] * nc for x in range(nr)]
    r = 0
    c = 0
    for i in range(0, nr*nc):
        A[r][c] = float(f.readline())
        c += 1
        if c == nc:
            c = 0
            r += 1

    return A


fnameA = sys.argv[1] if len(sys.argv) > 2 else "A.dat"
fnameX = sys.argv[2] if len(sys.argv) > 3 else "X.dat"


A = read(fnameA)
X = read(fnameX)
nrows = len(A)


QueueManager.register('get_queue')
QueueManager.register('out_queue')
m = QueueManager(address=('192.168.100.13', 8080), authkey=b'abracadabra')
m.connect()
queue = m.get_queue()
queue2 = m.out_queue()

print(nrows)
for w in range(nrows):
    queue.put((w, A[w], X))

print("wsadzone")


tasks_done = []
while(len(tasks_done) < nrows):
    l = queue2.get()
    tasks_done.append(l)


def takeId(elem):
    return elem[0]


tasks_done.sort(key=takeId)
result = []
for e in tasks_done:
    result.append(e[1])


# with open('output.txt', 'w') as filehandle:
#     json.dump(result, filehandle)
