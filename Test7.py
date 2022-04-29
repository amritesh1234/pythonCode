def solve(intervals):
    # Write your code here
    l = len(intervals)
    st = -1
    en = -1
    for i in intervals:
        count = 0
        for j in intervals:
            if j[0] <= i[0] <= j[1]:
                count += 1
        if count == l:
            st = i[0]
            break

    for i in intervals:
        count = 0
        for j in intervals:
            if j[0] <= i[1] <= j[1]:
                count += 1
        if count == l:
            en = i[1]
            break

    res = [st, en]
    return res

def solve1(intervals):
        s, e = zip(*intervals)
        return max(s), min(e)

print(solve1([
    [1, 100],
    [10, 50],
    [15, 65]
]))