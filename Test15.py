def solve(nums, target):
    # Write your code here
    a = sum(nums)
    b = target
    req = (a + b) // 2
    return subsetcount(nums, req)


def subsetcount(nums, req):
    rows = len(nums) + 1
    cols = req + 1
    t = [[0 for _ in range(cols)] for _ in range(rows)]

    zero_count = 0
    for i in nums:
        if i == 0:
            zero_count += 1

    for i in range(rows):
        t[i][0] = 2 ** zero_count

    for i in range(1, rows):
        for j in range(1, cols):
            if nums[i-1] <= j and nums[i-1] != 0:
                t[i][j] = t[i-1][j-nums[i-1]] + t[i-1][j]
            else:
                t[i][j] = t[i-1][j]
    return t[rows-1][cols-1]


nums = [1, 0]
k = solve(nums, 1)
print(12 == 12.0)
print(k)
