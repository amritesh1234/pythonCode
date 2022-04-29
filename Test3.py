from collections import Counter
import re

def solve(s, t):
    count = Counter(s)
    count.update(t)
    return all(v % 2 == 0 for v in count.values())

# print(solve("abc", "cba"))

def reg(s, n):
   p = '1,{}'.format(n)
   p = "{" + p + "}"
   pattern = '[a-z]'+p | '[A-Z]'+p
   return re.findall(pattern, s)

# print(reg("abcdefg", 3))

p = 'abc'
print(p + 'd')