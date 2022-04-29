def findPeak(arr, n):
    l = 0
    r = n - 1
    while l <= r:
        mid = l + (r - l) // 2
        if (l == 0 and r==0) or (l==n-1 and r==n-1):
            return arr[mid]
        elif arr[mid] > arr[mid - 1] and arr[mid] > arr[mid + 1]:
            return arr[mid]
        elif arr[mid] <= arr[mid + 1]:
            l = mid + 1
        else:
            r = mid - 1
    return -1

arr=[-17, 75, 34, 16, -88 ]
res = findPeak(arr, 5)
print(res)
