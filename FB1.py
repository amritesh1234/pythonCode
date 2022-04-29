def matching_pairs(s, t):
    # Write your code here
    sm = []
    tm = []
    max_till_now = float('-inf')
    l = len(s)
    if s == t and l > 1:
        return l - 2

    def update():
        nonlocal max_till_now
        currentCount = 0
        for i in range(l):
            if sm[i] == tm[i]:
                currentCount += 1
            if currentCount > max_till_now:
                max_till_now = currentCount

    for i in range(l):
        sm.append(s[i])
        tm.append(t[i])
    for i in range(l):
        if s[i] != t[i]:
            # currentCount = 0
            for j in range(i + 1, l):
                if s[j] != t[j]:
                    sm[i], sm[j] = sm[j], sm[i]
                    update()
                    # for i in range(l):
                    #    if sm[i] == tm[i]:
                    #      currentCount+=1
                    #  if currentCount > max_till_now:
                    #    max_till_now = currentCount
    return max_till_now

k = matching_pairs("abcd", "adcb")
print(k)