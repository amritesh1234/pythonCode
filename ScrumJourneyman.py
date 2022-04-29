def solve(intervals, types):
    res = []
    slot = set()
    for interval in intervals:
        slot.add(interval[0])
        slot.add(interval[1])
    slot = list(slot)
    slot.sort()
    for i in range(len(slot) - 1):
        currentSlot = []
        currentSlot.append(slot[i])
        currentSlot.append(slot[i + 1])
        currentSlot.append(0)
        res.append(currentSlot)

    for i, currentSlot in enumerate(res):
        for interval in intervals:
            if interval[0] < currentSlot[0] < interval[1] or interval[0] < currentSlot[1] < interval[1] or currentSlot[0:2] == interval:
                res[i][2] += 1
        if res[i][2] == 0:
            res.pop(i)
    return res

k = solve([
    [50, 127],
    [194, 274],
    [114, 157],
    [56, 92]
], [])
#print (k)

t = [(2,2,1),(1,1, 1),(2,1, 1),(1,0, 3), (1,0, 1)]
print (sorted(t))