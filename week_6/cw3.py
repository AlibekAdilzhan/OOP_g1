import unittest

class TestGetSum(unittest.TestCase):
    def test_1(self):
        res = get_sum([1, 2, 3])
        self.assertEqual(res, 6, "error test1")

    def test_2(self):
        res = get_sum([])
        self.assertEqual(res, 0, "empty list error")

    def test_3(self):
        res = get_sum([1])
        self.assertEqual(res, 1, "one element list")


def get_sum(mylist):
    s = 0
    for x in mylist:
        s += x
    return s

unittest.main()
