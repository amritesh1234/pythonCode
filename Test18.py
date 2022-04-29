class Tree:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def solve(root):
    # Write your code here
    if root is None:
        return 0
    q1 = []
    q2 = []
    q1.append(root)
    q = 1
    firstElement = True
    while len(q1) > 0 or len(q2) > 0:
        if q == 1:
            temp = q1.pop(0)
            if firstElement and not root.left and not root.right:
                sum += root.val
            firstElement = False
            if not q1:
                q = q2
                firstElement = True
            q2.append(temp.right)
            q2.append(temp.left)
        elif q == 2:
            temp = q2.pop(0)
            if firstElement and not root.left and not root.right:
                sum += root.val
            firstElement = False
            if not q2:
                q = q1
                firstElement = True
            q1.append(temp.right)
            q1.append(temp.left)
    return sum

n0 = Tree(5)
n0.left = Tree(3)
n0.right = Tree(6)
n0.left.left = Tree(2)
n0.left.right = Tree(4)

k = solve(n0)
print(k)