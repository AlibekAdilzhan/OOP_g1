import unittest

class TestGetSum(unittest.TestCase):
    def test_1(self):
        res = get_sum([1, 2, 3])
        self.assertEqual(res, 6, "something is wrong!")

    def test_2(self):
        res = get_sum([1])
        self.assertEqual(res, 1, "something is wrong!")

    def test_3(self):
        res = get_sum([])
        self.assertEqual(res, 0, "something is wrong!")


def get_sum(alist):
    s = 0
    for x in alist:
        s += x
    return s

unittest.main()