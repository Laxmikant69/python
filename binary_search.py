import numpy as np
arr = [87, 9, 13, 120, 14, 34]
def sorting(arr):
    arr.sort()
    return arr
print(sorting(arr))

def binary_search(arr, el, start, end):
    mid = (start + end) // 2
    if el == arr[mid]:
        return mid
    if el < arr[mid]:
        return binary_search(arr, el, start, mid-1)
    else:
        return binary_search(arr, el, mid+1, end)
print(binary_search(arr, 13, 0, len(arr)))



    
