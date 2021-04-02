from multiprocessing.managers import BaseManager
import queue


class QueueManager(BaseManager):
    pass


queue = queue.Queue()
QueueManager.register('get_queue', callable=lambda: queue)
m = QueueManager(address=('192.168.100.13', 80), authkey=b'abracadabra')
s = m.get_server()
s.serve_forever()
