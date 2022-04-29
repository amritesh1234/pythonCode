
class Tree:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class LLNode:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

def solve(root):
    # Write your code here
    # head = LLNode(1)
    return solveUtils(root)
    # return head


def solveUtils(root, pre):
    if not root:
        return
    solveUtils(root.left,  pre)
    if not pre :
       head = LLNode(root.val)
    else:
       pre.next =  LLNode(root.val)
    # head.next = LLNode(root.val)
    # head = head.next
    print (root.val, end=' ')
    solveUtils(root.right, pre)
    return head

n0 = Tree(1)
n0.left = Tree(0)
n0.right = Tree(2)
n0.left.left = Tree(3)
n0.left.right = Tree(4)

k = solve(n0)
print(k)