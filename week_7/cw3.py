import unittest
from cw1 import Queue

class TestQueue(unittest.TestCase):
    def setUp(self):
        self.q = Queue()
        self.q.append(1)
        self.q.append(2)

    def test_append(self):
        self.assertEqual(self.q.elms[0], 1)

    def test_peek(self):
        self.assertEqual(self.q.peek(), 1)

    def test_pop_front_1(self):
        self.q.pop_front()
        self.assertEqual(self.q.peek(), 2)
    
    def test_pop_front_1(self):
        a = self.q.pop_front()
        self.assertEqual(a, 1)
    

unittest.main()