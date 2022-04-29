def findPosition(arr, n, k):
    # Write your code here
    left = 0
    right = n - 1
    if arr[left] > arr[right]:
        l = left
        r = right
        while l <= r:
            mid = l + (r - l) // 2
            if mid == right:
                if arr[mid] == k:
                    return mid
                rightSearch = search(arr, 0, mid - 1, k)
                return rightSearch if rightSearch >= 0 else -1
            elif mid == 0:
                if arr[mid] == k:
                    return mid
                leftSearch = search(arr, mid + 1, n - 1, k)
                return leftSearch if leftSearch > 0 else -1
            elif arr[mid - 1] > arr[mid] and arr[mid] < arr[mid + 1]:
                leftSearch = search(arr, 0, mid - 1, k)
                rightSearch = search(arr, mid, n - 1, k)
                if leftSearch != -1:
                    return leftSearch
                else:
                    return rightSearch
            elif arr[mid] < arr[r]:
                if (r - l) == 1:
                    r = r - 1
                else:
                    r = mid

            else:
                if (r-l) == 1:
                    l = l+1
                else:
                    l = mid
    else:
        return search(arr, left , right , k)


def search(arr, l, r, k):
    while l <= r:
        mid = l + (r - l) // 2
        if arr[mid] == k:
            return mid
        elif arr[mid] < k:
            l = mid + 1
        else:
            r = mid - 1
    return -1

arr=[2, 4, 5, 6, 8, 9, 1]
# arr = [2]
# res = findPosition(arr,7, 2)
res = findPosition(arr,1, 2)
print(res)
print(max(arr))
