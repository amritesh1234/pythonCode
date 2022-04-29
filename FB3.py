from collections import deque

def findPositions(arr, x):
    # Write your code here
    q = deque()
    res = [None] * x
    a = 0
    for i, k in enumerate(arr):
        q.append((k, i))

    def getMaxIndex(q):
        print(x)
        mxIndex = -1
        originalIndex = -1
        max_till_now = float('-inf')
        for i in range(min(x, len(q))):
            if q[i][0] > max_till_now:
                max_till_now = q[i][0]
                mxIndex = i
                originalIndex = q[i][1]
            elif q[i][0] == max_till_now and originalIndex > q[i][1]:
                originalIndex = q[i][1]
                mxIndex = i
        return mxIndex, originalIndex

    while a < x and len(q) > 0:
        mxIndex, originalIndex = getMaxIndex(q)
        res[a] = originalIndex+1
        t = 0
        while t < x and len(q) > 0:
            temp = q.popleft()
            if t != mxIndex:
                if temp[0] > 0:
                  temp = (temp[0]-1, temp[1])
                q.append(temp)
            t += 1
        a += 1
    return res

arr = [1, 2, 2, 3, 4, 5]
k =  findPositions(arr, 5)
print(k)