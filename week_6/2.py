import unittest
import time

class TestBinSearch(unittest.TestCase):
    def test_1(self):
        res = binary_search([1, 2, 3, 4], 2)
        self.assertEqual(res, 1)
        time.sleep(1)

    def test_2(self):
        res = binary_search([1, 2, 3, 4], 5)
        self.assertEqual(res, -1)
        time.sleep(1)

    def test_3(self):
        res = binary_search([], 1)
        self.assertEqual(res, -1)
        time.sleep(1)
        
    def test_4(self):
        res = binary_search([1], 1)
        self.assertEqual(res, 0)
        time.sleep(1)



def binary_search(mylist, x):
    n = len(mylist)
    if n == 0:
        return -1
    a, b = 0, n - 1
    while True:
        mid = (a + b) // 2
        if mylist[mid] == x:
            return mid
        elif mylist[mid] < x:
            a = mid + 1
        else:
            b = mid
        if a == b and mylist[mid] != x:
            return -1


unittest.main()
