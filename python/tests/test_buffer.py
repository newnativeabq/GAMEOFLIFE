#test_queue.py



import unittest


from render import Buffer, Writer, Reader
# from multiprocessing import Queue
from queue import Queue


class TestBuffer(unittest.TestCase):
    
    def setUp(self):
        self.maxsize = 20
        self.buffer = Buffer(maxsize=self.maxsize)
        self.qtest = Queue()


    def test_writer(self):
        w = Writer(self.qtest)
        for i in range(10):
            w(i)
        self.assertEqual(self.qtest.get(), 0)



    def test_reader(self):
        r = Reader(self.qtest)
        for i in range(10):
            self.qtest.put(i)

        contents = [r() for _ in range(10)]
        self.assertEqual(10, len(contents))
        assert r() is None


    def test_fill_buffer(self):
        for _ in range(self.maxsize):
            self.buffer.put('emptyput')
        self.buffer.teardown()