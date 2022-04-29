from collections import deque
def solve(n):
    low = 0
    high = n - 1
    while low <= high:
        mid = (low + high) // 2
        if low == high or mid * mid == n:
            return mid
        if mid * mid > n:
            high = mid - 1
        else:
            low = mid + 1
    if(high < low) :
        return high



def solve( path):
        # Write your code here
        st = deque()
        for i in path:
            if i == '..':
                st.pop()
            elif i == '.':
                pass
            else:
                st.append(i)
        return list(len(st))
        # return ' '.join(st)

# print(solve(["usr","..","usr",".","local","bin","docker"]))


def solve(s, i, j):
    # Write your code here
    st = i % len(s)
    end = j % len(s)

    if st == end:
        fr = (j - i) // len(s)
        temp = s[st:] + s[:st]
        return temp * int(fr)
    else:
        return s[st:end]

# print(solve('tiger', 6, 8))
print(solve('hi', 2, 6))

s = "abc"
print(s.rep)
