#__author__ = ritvikareddy2
#__date__ = 2019-02-16


class Node:

    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def isRoot(flag):
    return flag == 0

def isLeaf(node):
    return node.left is None and node.right is None


def isLeftBoundary(flag):
    return flag == 1


def isRightBoundary(flag):
    return flag == 2


def getLeftChildFlag(parent, pflag):
    if isLeftBoundary(pflag) or isRoot(pflag):
        return 1

    elif isRightBoundary(pflag) and parent.right is None:
        return 2

    return 3


def getRightChildFlag(parent, pflag):

    if isRightBoundary(pflag) or isRoot(pflag):
        return 2

    elif isLeftBoundary(pflag) and parent.left is None:
        return 1

    return 3


def boundary(root):
    if not root:
        return
    left_boundary = []
    right_boundary = []
    leaves = []
    stack = [(root, 0)]

    # flags 0=root, 1=leftboundary, 2=rightboundary, 3=others

    while stack:
        curr, flag = stack.pop()
        if not curr:
            break

        if isLeftBoundary(flag) or isRoot(flag):
            left_boundary.append(curr.val)

        elif isRightBoundary(flag):
            right_boundary.append(curr.val)

        elif isLeaf(curr):
            leaves.append(curr.val)

        if curr.right is not None:
            rflag = getRightChildFlag(curr, flag)
            stack.append((curr.right, rflag))

        # add only those left nodes which are part of left boundary
        if curr.left is not None:
            lflag = getLeftChildFlag(curr, flag)
            stack.append((curr.left, lflag))


    return left_boundary + leaves + right_boundary[::-1]


if __name__ == '__main__':
    root = Node(1)

    root.left = Node(2)
    root.right = Node(3)

    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.left = Node(6)

    root.left.right.left = Node(7)
    root.left.right.right = Node(8)
    root.right.left.left = Node(9)
    root.right.left.right = Node(10)
    print(boundary(root))