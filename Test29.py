from collections import Counter
import heapq
import itertools

def findIndex(S, W):
    ls = len(S)
    lw = len(W)
    res = []

    def isAnagram(str, W):
        return Counter(str) == Counter(W)

    for i in range(ls-lw+1):
        str = S[i:i+lw]
        if (isAnagram(str, W)):
            res.append(i)
    return res

# k = findIndex("abxaba", "ab")
# print(k)

def regular_numbers(n):
    solution = [1]
    last = 0; count = 0

    while count < n:
        x = heapq.heappop(solution)
        if x > last:
            yield x
            last = x; count += 1
            heapq.heappush(solution, 2 * x)
            heapq.heappush(solution, 3 * x)
            heapq.heappush(solution, 5 * x)


def look_and_say(num):
    result = '1'

    for _ in range(num - 1):
        tmp = ''
        for char, group in itertools.groupby(result):
            count = len(list(group))
            tmp += (str(count) + char)
        result = tmp

    return result


test_string = "GeeksforGeeks is best for geeks"
spl_word = 'best'
res = test_string.partition(spl_word)[1]
print(res)


def possible(piles, H, K) :
    time = 0
    for  p in piles:
       time += (p - 1) / K + 1;
    return time <= H