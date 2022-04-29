def allocateBooks(arr, n, m):
    # Write your code here
    # Return the minimum number of pages
    if (n < m):
        return -1

    low = max(arr)
    totalPages = sum(arr)
    res = totalPages
    l = low
    r = totalPages
    while (l <= r):
       mid = l + (r - l) // 2
       if conditionsSatisfy(arr, mid, m):
          res = min(res, mid)
          r = mid - 1
       else:
          l = mid + 1
    return res


def conditionsSatisfy(arr, mid, m):
    student = 1
    reqSum = mid
    for x in arr:
        if x <= reqSum:
            reqSum = reqSum - x
        else:
            student += 1
            reqSum = mid - x
    if (student > m):
        return False
    return True


arr=[12 ,34, 67, 90]
res = allocateBooks(arr, 4, 2)
print(res)


