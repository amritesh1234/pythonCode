def shiftedBinarySearch(array, target):
    # Write your code here.
    if len(array) == 0:
        return -1
    # ref = rotate()
    rotatedIndex = findmid(array)
    left = search(array, 0, rotatedIndex - 1, target)
    right = search(array, rotatedIndex, len(array) - 1, target)
    if left != -1:
        return left
    elif right != -1:
        return right
    else:
        return -1


def findmid(array):
    N = len(array)
    low = 0
    high = len(array) - 1
    while low <= high:
        mid = low + (high - low) // 2
        pre = (mid + N - 1) % N
        nex = (mid + 1) % N
        if (array[mid] < array[pre] and array[mid] <= array[nex]) or (array[mid] <= array[pre] and array[mid] < array[nex]):
            return mid
        elif array[mid] > array[high]:
            low = mid
        elif array[mid] <= array[low]:
            high = mid

    return -1


def search(array, low, high, target):
    while low <= high:
        mid = low + (high - low) // 2
        if array[mid] == target:
            return mid
        elif array[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1

arr  = [72, 73, 0, 1, 21, 33, 37, 45, 61, 71]
k = shiftedBinarySearch(arr, 72)
print(k)