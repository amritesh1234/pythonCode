from collections import deque


class Tree:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def solve(node0, node1):
    # Write your code here
    # result = Tree(0)
    m = solveUtil(node0, node1)
    return m


def solveUtil(node0, node1):
    # Write your code here
    result = Tree(0)
    if not (node0 or node1):
        return None

    if node0 and node1:
        result = Tree(node0.val + node1.val)
    elif node0:
        result = Tree(node0.val)
    elif node1:
        result = Tree(node1.val)

    if node0.left and node1.left:
        result.left = solveUtil(node0.left, node1.left, result)
    elif node0.left:
        result.left = node0.left
    else:
        result.left = node1.left

    if node0.right and node1.right:
        result.right = solveUtil(node0.right, node1.right, result)
    elif node0.right:
        result.right = node0.right
    else:
        result.right = node1.right

    return result


n0 = Tree(1)
n0.left = Tree(0)
n0.right = Tree(2)

n1 = Tree(1)

# stack = deque()
# stack.pop()


# k = solve(n0, n1)
# print(k)


def solve1(root):
    # Write your code here
    st = deque()
    st.append(root)
    flag = False

    while st:
        temp = st.popleft()
        if not temp:
            flag = True
        elif flag and temp:
            return False
        else:
            st.append(temp.left)
            st.append(temp.right)
    return True


k = solve1(n0)
print(k)
