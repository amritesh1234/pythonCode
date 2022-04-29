friends = [
    [0, 1],
    [1, 0, 2],
    [2, 1],
    [3, 4],
    [4, 3],
    [5]
]

temp = []
for f in friends:
    temp.extend(f)
# print(list(set(temp)))


def depthSum(nestedList):
    totalSum = 0
    def util(lst, currentDepth):
        temp = 0
        for element in lst:
            if isinstance(element, list):
                temp += util(element, currentDepth + 1)
            else:
                temp += currentDepth * element
        return temp

    for element in nestedList:
        if type(element) is list:
            totalSum += util(element, 2)
        else:
            totalSum += element
    return totalSum

k = depthSum([1,[4,[6]]])
# print(k)


l = [[1,1],2,[1,1]]

