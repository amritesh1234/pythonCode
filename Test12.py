class Tree:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def solve(self, root):
        # Write your code here
        node = root
        k = self.getNumberOfEvenLeaves(node)
        while k > 0:
            self.deleteLeaveNodes(node, None, 0)
            if node.left is None and node.right is None and (root.val % 2 == 0):
                return None
        return node

    def getNumberOfEvenLeaves(self, node):
        if node is None:
            return 0
        if node.left is None and node.right is None and (node.val % 2 == 0):
            return 1
        return self.getNumberOfEvenLeaves(node.left) + self.getNumberOfEvenLeaves(node.right)

    def deleteLeaveNodes(self, node, parent, t):
        if node is None:
            return
        if node.left is None and node.right is None and (node.val % 2 == 0):
            if t < 0 :
                parent.left = None
            elif t > 0 :
                parent.right = None
            else :
                return
        self.deleteLeaveNodes(node.left, node, -1)
        self.deleteLeaveNodes(node.right, node, 1)


n0 = Tree(2)
n0.left = Tree(0)

k = Solution().solve(n0)
print(k)