from collections import deque


class Tree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def iterativeInOrderTraversal(tree):
    # Write your code here.
    st = deque()
    # st.append(tree)
    temp = tree
    while temp or st:
        while temp:
            st.append(temp)
            temp = temp.left
        temp = st.pop()
        print(temp.value)
        temp = temp.right


n0 = Tree(5)
n0.left = Tree(3)
n0.right = Tree(6)
n0.left.left = Tree(2)
n0.left.right = Tree(4)

iterativeInOrderTraversal(n0)
# print(k)
