from heapq import heapify, heappop
import math
import bisect

def solve(cells):
        # Write your code here
        res, first = -1, -1
        if not cells:
            return res
        for i in range(len(cells)):
            cells[i] = -1 * cells[i]
        heapify(cells)

        res = (-1 * heappop(cells))
        while cells:
            second = (-1 * heappop(cells))
            if res == second:
                if cells :
                  res= (-1 * heappop(cells))
                else :
                  res = -1
            else:
                res = math.floor((res + second) / 3)
        return res

# print(solve([854, 389, 789, 239, 682, 994]))
# print(solve([10, 30, 30, 20]))

def inserElement() :
    li = [1, 3, 4, 4, 4, 6, 7]
    # li.reverse()
    print(li)
    print(li.pop())
    # print(bisect.insort(li, 5))
    print(li)

inserElement()