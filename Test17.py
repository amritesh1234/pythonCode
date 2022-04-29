class Tree:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def solve(self, root, lo, hi):
        # Write your code here
        self.key = []
        self.getKeysToBeDeleted(root, lo, hi)
        for k in self.key:
            self.deleteNode(root, k)

    def getKeysToBeDeleted(self, root, lo, hi):
        if root is None:
            return
        if root.val > lo and root.val < hi:
            self.key.append(root.val)
        self.getKeysToBeDeleted(root.left, lo, hi)
        self.getKeysToBeDeleted(root.right, lo, hi)

    def deleteNode(self,root, key):
        if root is None:
            return root
        if key < root.val:
            root.left = self.deleteNode(root.left, key)
        elif (key > root.val):
            root.right = self.deleteNode(root.right, key)
        else:
            if not root.left and not root.right:
                root = None
            elif not root.left:
                root = root.right
            elif not root.right:
                root = root.left
            else:
                temp = self.deleteNode()
                root.val = temp.val
                root.right = self.deleteNode(root.right, temp.val)

    def minValueNode(self, node):
        current = node
        while (current.left is not None):
            current = current.left
        return current

n0 = Tree(5)
n0.left = Tree(3)
n0.right = Tree(6)
n0.left.left = Tree(2)
n0.left.right = Tree(4)

k = Solution().solve(n0, 2, 5)
print(k)