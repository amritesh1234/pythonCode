def missingNumber(arr, n):
    # Write your code here
    # Return a single integer
    givenSum = sum(arr)
    d = getDifference(arr)
    total = (n+1)*(2*arr[0] + n*d)//2
    return total-givenSum

def getDifference(arr):
    seen = set()
    seen.add(arr[1]-arr[0])
    last = 1
    for i in range(2, len(arr)):
        nextDiff = arr[i]-arr[last]
        if nextDiff in seen:
            return nextDiff
        seen.add(nextDiff)
        last = i
    return min(seen)

arr=[1, 4, 10]
# res=missingNumber(arr, 3)
# print(res)


def smartInterval(intervals, n):
    # Write your code here.
    first = {}
    li = set()
    ans=[]
    for i, interval in enumerate(intervals):
        first[interval[0]] = i
        li.add(interval[0])
    li = sorted(li)
    for val in intervals:
        i = search(val[1], li)
        if i >= 0:
            ans.append(first[val[1]])
        else:
            ans.append(-1)
    return ans

def search(element, arr):
    l = 0
    r = len(arr) - 1
    while l <= r:
        mid = l + (r - l) // 2
        if arr[mid] == element:
            return mid
        elif arr[mid] < element:
            l = mid + 1
        else:
            r = mid - 1
    return -1


arr=[[1,2], [2,3], [3,4]]
res=smartInterval(arr, 3)
print(res)


