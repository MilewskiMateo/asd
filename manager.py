from multiprocessing.managers import BaseManager
import queue


class QueueManager(BaseManager):
    pass


queue1 = queue.Queue()
queue2 = queue.Queue()
QueueManager.register('get_queue', callable=lambda: queue1)
QueueManager.register('out_queue', callable=lambda: queue2)
m = QueueManager(address=('192.168.100.13', 8080), authkey=b'abracadabra')
s = m.get_server()
s.serve_forever()
