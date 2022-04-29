from collections import deque
import random
class Solution:
    def solve(self, nums, k):
        if len(nums) < k:
            return -1
        res = []
        q = deque()
        counter = 0
        max = float("-inf")
        for i in range(len(nums)):
            if counter < k:
                counter+=1
                if max < nums[i]:
                    max = nums[i]
                    maxindex=i
            else:
                if not q:
                    q.append(maxindex)
                while q :
                    if q[0] <= i-k:
                        q.popleft()
                if not q and (nums[i] < nums[q[-1]]):
                    q.append(i)
                else:
                    while nums[q[-1]] < nums[i]:
                        q.pop()
                res.append(nums[q[0]])
        return res


nums = [10, 5, 2, 7, 8, 7]
k = 3
res = Solution().solve(nums, k)
print(res)

random.randint(0,30)