import numpy as np

# sorting
arr = [87, 9, 13, 120, 14, 34]
def sorting(arr):
    arr.sort()
    return arr
print(sorting(arr))


# Binary search
def binary_search(arr, el, start, end):
    mid = (start+end) // 2
    if el == arr[mid]:
        return mid
    elif el < arr[mid]:
        return binary_search(arr, el, start, mid-1)
    elif arr!= el:
        return ("element is not present in the array")
    else:
        return binary_search(arr, el, mid+1, end)
        
print(binary_search(arr, 13, 0, len(arr)))


"""# Binary Search in python


def binarySearch(array, x, low, high):

    # Repeat until the pointers low and high meet each other
    while low <= high:

        mid = low + (high - low)//2

        if array[mid] == x:
            return mid

        elif array[mid] < x:
            low = mid + 1

        else:
            high = mid - 1

    return -1


array = [3, 4, 5, 6, 7, 8, 9]
x = 4

result = binarySearch(array, x, 0, len(array)-1)

if result != -1:
    print("Element is present at index " + str(result))
else:
    print("Not found")


# Merging
def merging():
    a = [1, 2, 3, 4, 5]
    b = [7, 8, 9, 5]
    merged_list = np.concatenate((a, b))
    return merged_list
print(merging())


#Revrsing
def rev ():
    rev_list = np.flipud(arr)
    return rev_list
print(rev())"""
