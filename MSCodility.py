from heapq import heapify, heappush, heappop

def solution(A, B, C):
    # write your code in Python 3.6
    dict = {}
    dict["a"] = A
    dict["b"] = B
    dict["c"] = C
    sortedItemsFrequencyPair = sorted(dict.items(), key=lambda x : x[1], reverse=True)
    resultString = ""
    p = sortedItemsFrequencyPair[0][0]
    while (dict["a"] + dict["b"] + dict["c"] != 0):
        x = 0
        if (p == sortedItemsFrequencyPair[0][0]):
            while (dict[p] != 0 and x != 2):
                resultString = resultString + p
                dict[p] = dict[p] - 1
                x = x + 1
        else:
            if (dict[sortedItemsFrequencyPair[0][0]] % 2 == 0):
                n = dict[sortedItemsFrequencyPair[0][0]] / 2
            else:
                n = int(dict[sortedItemsFrequencyPair[0][0]] / 2) + 1
            if (dict[p] <= n or dict[p] < 2):
                resultString = resultString + p
                dict[p] = dict[p] - 1
            else:
                resultString = resultString + p + p
                dict[p] = dict[p] - 2
        if (p == "a"):
            if (dict["b"] == 0 and dict["c"] == 0):
                break
            elif (dict["b"] >= dict["c"]):
                p = "b"
            elif (dict["b"] < dict["c"]):
                p = "c"
        elif (p == "b"):
            if (dict["a"] == 0 and dict["c"] == 0):
                break
            elif (dict["a"] >= dict["c"]):
                p = "a"
            elif (dict["a"] < dict["c"]):
                p = "c"
        else:
            if (dict["a"] == 0 and dict["b"] == 0):
                break
            elif (dict["a"] >= dict["b"]):
                p = "a"
            elif (dict["a"] < dict["b"]):
                p = "b"
    return (resultString)


def isValidBST(root):
    ans = True

    def traverse(node):
        global ans
        if not node:
            return float('inf'), float('-inf')

        lmin, lmax = traverse(node.left)
        rmin, rmax = traverse(node.right)

        if node.val <= lmax or node.val >= rmin:
            ans = False
        return min(lmin, node.val), max(rmax, node.val)
    traverse(root)
    return ans


def explore(node, low, high):
    if not low < node.val < high:
        return False
    if node.left:
        new_high = node.val
        if not explore(node.left, low, new_high):
            return False
    if node.right:
        new_low = node.val
        if not explore(node.right, new_low, high):
            return False
    return True

# print(solution(6, 1, 1))


from collections import Counter

def solution(a):
    allPossibleSubstring = []
    dictionary = dict()
    singleFrequencySubstringLengthlist = []
    stringWithFrequenceyOne = []

    for i in range(len(a)):
        for j in range(i + 1, len(a)):
            if i != j:
                allPossibleSubstring.append(a[i:j + 1])

    allSubstringCounter = Counter(allPossibleSubstring)

    for i in allSubstringCounter:
        if allSubstringCounter[i] == 1:
            stringWithFrequenceyOne.append(i)

    for i in range(len(stringWithFrequenceyOne)):
        dictionary[stringWithFrequenceyOne[i]] = len(stringWithFrequenceyOne[i])

    for i in dictionary:
        singleFrequencySubstringLengthlist.append(dictionary[i])
    return (min(singleFrequencySubstringLengthlist))

def test():
    lookup = {}
    lookup['a'] = [1, 0, 2]
    lookup['b'] = [4, 6, 9]
    print(lookup)
    print( list(lookup)[1] )
    print(lookup.keys())
    print(lookup.values())

/Users/amritesh.singh/myPython/MSCodility.py






