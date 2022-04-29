import copy
def subsets(nums):
    res = []
    rset = []
    n = len(nums)
    def formset(nums, n, curIndex, res, rset):
        # if curIndex == n:
        r = copy.deepcopy(rset)
        res.append(r)

        for i in range(curIndex,n):
            rset.append(nums[i])
            formset(nums, n, i + 1, res, rset)
            rset.pop()

    formset(nums, n, 0, res, rset)
    return res

# nums = [1,2,3]
# print(subsets(nums))


def subsets1(nums):
    res = []
    rset = []
    n = len(nums)
    def formset(nums, n, curIndex, res, rset):
        runningset = copy.deepcopy(rset)
        res.append(runningset)
        for i in range(curIndex, n):
            rset.append(nums[i])
            formset(nums, n, i + 1, res, rset)
            rset.pop()

    formset(nums, n, 0, res, rset)
    return res

nums = [1,2,3]
print(subsets1(nums))



class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        rset=[]
        res = []
        n = len(nums)
        used = [False]*n
        def solve(nums, n, currIndex, rset, res, used):
            if currIndex == n:
                runningset = copy.deepcopy(rset)
                res.append(runningset)
            for i in range(n):
                if used[i] == False:
                   rset.append(nums[i])
                   used[i] = True
                   solve(nums, n, currIndex+1, rset, res, used)
                   rset.pop()
                   used[i] = False
        solve(nums, n, 0, rset, res, used)
        return res