def bubble_sort(array):
    n = len(array)
    for i in range(n):
        for j in range(n - i - 1):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
            
    return array


def merge_sort(array):
    n = len(array)
    if n > 1:
        mid = n // 2    
        left_arr = array[:mid]
        right_arr = array[mid:]
        merge_sort(left_arr)
        merge_sort(right_arr)

        i, j, k = 0, 0, 0
        while i < len(left_arr) and j < len(right_arr):
            if left_arr[i] < right_arr[j]:
                array[k] = left_arr[i]
                i += 1
            else:
                array[k] = right_arr[j]
                j += 1
            k += 1

        while i < len(left_arr):
            array[k] = left_arr[i]
            k += 1
            i += 1
        
        while j < len(right_arr):
            array[k] = right_arr[j]
            k += 1
            j += 1




array = [1, 2, 1, 0, 0, 1]
merge_sort(array)
print(array)