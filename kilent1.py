from multiprocessing.managers import BaseManager
import sys


class QueueManager(BaseManager):
    pass


QueueManager.register('get_queue')
m = QueueManager(address=('192.168.100.1', 80), authkey=b'abracadabra')
m.connect()
queue = m.get_queue()
queue.put(sys.argv[1])
