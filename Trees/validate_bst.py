#__author__ = ritvikareddy2
#__date__ = 2019-02-16


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def isValidBST(root):
    """
    :type root: TreeNode
    :rtype: bool
    """
    if not root:
        return True

    stack = [(root, None, None)]

    while stack:
        curr, low, high = stack.pop()
        if curr.right:
            if curr.right.val > curr.val:
                if high and curr.right.val >= high:
                    return False
                stack.append((curr.right, curr.val, high))
            else:
                return False
        if curr.left:
            if curr.left.val < curr.val:
                if low and curr.left.val <= low:
                    return False
                stack.append((curr.left, low, curr.val))
            else:
                return False
    return True


