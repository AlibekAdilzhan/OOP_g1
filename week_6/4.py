
def get_partial_sums(mylist):
    sums = []
    for i in range(len(mylist) - 1):
        s = 0
        for j in range(i, len(mylist)):
            s += mylist[j]
        sums.append(s)
    return sums


mylist = [1, 2, 3, 4, 5, 6]
print(get_partial_sums(mylist))

