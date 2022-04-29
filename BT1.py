import copy

def partition(s):
    mainRes = []
    def isPalindrome(st):
        i = 0
        j = len(st) - 1
        while i < j:
            if st[i] != st[j]:
                return False
            else:
                i+=1
                j-=1
        return True

    def partitionUtil(st, tempRes):
        if len(st) == 0 or st == '':
            mainRes.append(copy.deepcopy(tempRes))
            return
        for i in range(1,len(st)+1):
            leftSubstring = st[0:i]
            if isPalindrome(leftSubstring):
                tempRes.append(leftSubstring)
                rightSubstring = st[i:len(st)]
                partitionUtil(rightSubstring, tempRes)
                tempRes.pop()

    t = []
    partitionUtil(s, t)
    return mainRes

k = partition("radar")
print(k)




