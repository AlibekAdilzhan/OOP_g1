import unittest

class TestQueue(unittest.TestCase):
    def test_append(self):
        q = Queue()
        q.append(1)
        self.assertEqual(q.elms[0], 1)

    def test_peek(self):
        q = Queue()
        q.append(2)
        self.assertEqual(q.peek(), 2)

    def test_pop_front_1(self):
        q = Queue()
        q.append(1)
        q.append(2)
        q.pop_front()
        self.assertEqual(q.peek(), 2)
    
    def test_pop_front_1(self):
        q = Queue()
        q.append(1)
        q.append(2)
        a = q.pop_front()
        self.assertEqual(a, 1)
    

class Queue:
    def __init__(self):
        self.elms = []

    def append(self, x):
        self.elms.append(x)

    def pop_front(self):
        # if self.is_empty():
            # raise AttributeError("there are no elements in the queue")
        return self.elms.pop(0)

    def is_empty(self):
        if self.elms == []:
            return True
        else:
            return False

    def peek(self):
        if self.is_empty():
            raise AttributeError("there are no elements in the queue")
        return self.elms[0]
    
    def size(self):
        return len(self.elms)

    def __str__(self):
        return f"{self.elms}"

unittest.main()