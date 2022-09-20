# Here is a demo of quick sort algorithm

import random


def quick_sort(arr):
    if len(arr) < 2:
        return arr
    else:
        pivot = arr[0]
        less = [i for i in arr[1:] if i <= pivot]
        greater = [i for i in arr[1:] if i > pivot]
        return quick_sort(less) + [pivot] + quick_sort(greater)

unsorted_arr = []
for i in range(100):
    unsorted_arr.append(random.randint(1, 100))

print("Unsorted array: ", unsorted_arr)
print("Sorted array: ", quick_sort(unsorted_arr))