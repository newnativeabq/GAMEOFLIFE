"""
Buffer
    Queue implementation for asynchronous game state generation.
"""


from queue import Queue
# from multiprocessing import Process, Queue






def _set_value(key:str, lookup:dict, default):
    if key in lookup:
        return lookup[key]
    return default




class Writer():
    def __init__(self, q):
        self.q = q

    def __call__(self, item):
        self.q.put(item)


class Reader():
    def __init__(self, q):
        self.q = q

    def __call__(self):
        if not self.q.empty():
            return self.q.get()
        return None



class Buffer():
    def __init__(self, *args, **kwargs):
        self.q, self.w, self.r = self._build_queue_stack()

    def _build_queue_stack(self):
        newQ = Queue()
        return newQ, Writer(newQ), Reader(newQ)


    def put(self, package):
        self.w(package)


    def get(self):
        return self.r()


    def teardown(self):
        del self.q 
        self.q, self.w, self.r = self._build_queue_stack()


    @property
    def size(self):
        return self.q.qsize()


