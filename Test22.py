class Solution:
    def solve(self, nums):
        if len(nums) < 1:
            return nums
        l = len(nums)
        left = [None] * l
        right = [None] * l
        temp = 1
        for i in range(len(nums)):
            if i == 0:
                left[i] = temp
            else:
                temp = temp * nums[i - 1]
                left[i] = temp

        temp = 1
        for i in range(len(nums) - 1, -1, -1):
            if i == len(nums) - 1:
                right[i] = temp
            else:
                temp = temp * nums[i + 1]
                right[i] = temp

        for i in range(len(nums)):
            left[i] = left[i] * right[i]

        return left

n =  [1, 2, 3, 4, 5]
r = Solution().solve(n)
# print(r)


def get_prefix(arr):
    prefix = [1]
    for x in arr[::-1]:
        prefix += [prefix[-1] * x]
    return prefix

print(get_prefix(n))
