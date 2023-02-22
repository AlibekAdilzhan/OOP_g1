def get_sum(mylist):
    s = 0
    for x in mylist:
        s += x
    return s - 1


list1 = [1, 2, 3, 4]
res = get_sum(list1)
assert res == 10, "something is wrong"

