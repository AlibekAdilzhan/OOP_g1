def bubble_sort(array):
    n = len(array)
    for i in range(n):
        for j in range(n - i - 1):
            if array[j] < array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
            
    return array



arrival = [2.00, 2.10, 3.00, 3.20, 3.50, 5.00]
departure = [2.30, 3.40, 3.20, 4.30, 4.00, 5.20]

arrival.sort()
departure.sort()

i, j = 0, 0
trains_num = 0
plats_num = 0

while i < len(arrival):
    if arrival[i] < departure[j]:
        trains_num += 1
        plats_num = max(plats_num, trains_num)
        i += 1

    else:
        trains_num -= 1
        j += 1

print(plats_num)