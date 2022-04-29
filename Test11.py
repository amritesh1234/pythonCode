class Tree:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self, max):
        self.max = max

    def solve(self, root):
        # Write your code here
        k = self.solveUtils(root, 0, 0)
        return self.max

    def solveUtils(self, root, ls, rs):
        if root is None:
            return ls, rs

        if root.left is not None:
            ls += root.left.val
        l = self.solveUtils(root.left, ls, rs)

        if root.right is not None:
            rs += root.right.val
        r = self.solveUtils(root.right, ls, rs)

        t1, t2 = 0, 0
        if root.left is not None:
           t1 = root.left.val

        if root.right is not None:
           t2 = root.right.val

        if max((t1 + l[0]), (t1 + r[0]),
           (t2 + l[1]), (t2 + r[1])) > self.max:
           self.max = max((t1 + l[0]), (t1 + r[0]),
                  (t2 + l[1]), (t2 + r[1]))
        return t1, t2


def findMaxUtil(root):
    # Base Case
    if root is None:
        return 0

    l = findMaxUtil(root.left)
    r = findMaxUtil(root.right)

    max_single = max(max(l, r) + root.val, root.val)
    max_top = max(max_single, l + r + root.val)

    findMaxUtil.res = max(findMaxUtil.res, max_top)
    return max_single


def findMaxSum(root):
    findMaxUtil.res = float("-inf")
    findMaxUtil(root)
    return findMaxUtil.res


n0 = Tree(5)
n0.left = Tree(2)
# n0.right = Tree(2)
# n0.left.left = Tree(3)
# n0.left.right = Tree(4)

k = findMaxSum(n0)
print(k)
