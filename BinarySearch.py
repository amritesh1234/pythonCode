arr = [1, 4, 5, 8, 10, 10, 10, 10, 10, 14, 17, 19, 22]

def binarySearch(arr, k):
    if len(arr) == 0:
        return -1
    low = 0
    high = len(arr)-1
    while low <= high:
        mid = low + (high-low)//2
        if arr[mid] >= k:
            result = high
            high = mid - 1
        elif arr[mid] < k:
            low = mid+1
    return result

def binarySearch2(arr, k):
    if len(arr) == 0:
        return -1
    low = 0
    high = len(arr)-1
    while low <= high:
        mid = low + (high-low)//2
        if arr[mid] > k:
            high = mid - 1
        elif arr[mid] <= k:
            result = high
            low = mid+1
    return result

l = binarySearch2(arr, 10)
print(l)

