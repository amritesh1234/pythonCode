class Tree:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def solve(root):
    # Write your code here
    return solveUtil(root, True)


def solveUtil(root, result):
    if not (root.left or root.right):
        return result
    lv, rv = 0, 0
    if root.right:
        rv = root.right.val
    if root.left:
        lv = root.left.val
    if (rv + lv) != root.val:
        result = False
        return result
    return result and solveUtil(root.left, result) and solveUtil(root.right, result)


root = Tree(19)
root.left = Tree(9)
root.right = Tree(10)
root.left.right = Tree(3)
root.right.left = Tree(16)
root.right.right = Tree(24)
# root.left = Tree(1)
# root.right = Tree(8)
# root.right.left = Tree(6)
# root.right.right = Tree(2)
# root.right.left.left = Tree(6)
# print(solve(root))
print(solve(root))