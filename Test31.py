def aggressiveCows(stalls, k):
    # Write your code here.
    stalls = sorted(stalls)
    n = len(stalls)
    if k > n:
        return -1
    l = 0
    r = stalls[-1]
    result = float("-inf")
    while l <= r:
        mid = l + (r - l) // 2
        if isPossible(stalls, k, mid):
            result = max(result, mid)
            l = mid + 1
        else:
            r = mid - 1
    return result


def isPossible(stalls, k, mid):
    placed = 1
    lastIndex = stalls[0]
    for x in stalls:
        if x-lastIndex >= mid:
            placed += 1
            lastIndex = x
    if placed < k:
        return False
    return True


arr=[87, 93, 51, 81, 68, 99, 59]
res = aggressiveCows(arr, 4)
print(res)




