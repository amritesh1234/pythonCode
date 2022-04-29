def addStrings(num1: str, num2: str) -> str:
    modnum1 = num1[::-1]
    modnum2 = num2[::-1]
    ans = ""
    carry = 0
    l1 = len(num1)
    l2 = len(num2)
    maxlen = max(l1, l2)
    c1, c2 = 0, 0
    for i in range(maxlen):
        if c1 < l1 and c2 < l2:
            curr = int(modnum1[i]) + int(modnum2[i]) + carry
            c1 += 1
            c2 += 1
        elif c1 > l1 and c2 < l2:
            curr = int(modnum2[i]) + carry
            c2 += 1
        elif c2 > l2 and c1 < l1:
            curr = int(modnum1[i]) + carry
            c1 += 1
        if curr > 9:
            carry = 1
            curr = curr % 10
        else:
            carry = 0
        ans = ans + str(curr)
    if carry == 1:
        ans = ans + '1'
    return ans[::-1]

# k = addStrings("9", "99")
# print(k)

# l = [[1, 2], [3, 4]]
# a = [6, 7]
# res = []
# for _, set in enumerate(l):
#      res.append(a + set)
# print (res)

# k=2
# arr = [1,2,4,3,2,4,1,1,1]
# s= set(arr)
# std = sorted(s)
# print(std[0:k])

def get_largest_value(nums):
    nums = [str(x) for x in nums]
    length = len(max(nums, key=len))

    normalized = []
    for i, x in enumerate(nums):
        element = x * (length // len(x) + 1)
        normalized.append(element[:length])

    ordered = sorted(zip(nums, normalized), key=lambda x: x[1], reverse=True)

    return ''.join([x[0] for x in ordered])

# print(get_largest_value([10, 7, 76, 415]))

for i in range(4,5):
    print(i)

