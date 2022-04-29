import collections

class Tree:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def solve(self, root):
        # Write your code here
        dict = {}
        collections.Counter().most_common()

        def traverse(node, height):
            if node is None:
                return
            if height in dict.keys():
                dict[height] += node.val
            else:
                dict[height] = node.val
            traverse(node.left, height + 1)
            traverse(node.right, height + 1)

        traverse(root, 0)
        min1 = dict[0]
        res = 0
        for k in dict.keys():
            if dict[k] < min1:
                min1 = dict[k]
                res = k
        return res


n0 = Tree(5)
n0.left = Tree(2)
n0.left.left = Tree(0)
n0.left.right = Tree(6)
n0.right = Tree(3)
n0.right.right = Tree(1)

d = Solution().solve(n0)
print(d)
