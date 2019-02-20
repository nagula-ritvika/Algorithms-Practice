#__author__ = ritvikareddy2
#__date__ = 2019-02-16

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def inorderSuccessor(root, p):
    """
    :type root: TreeNode
    :type p: TreeNode
    :rtype: TreeNode
    """
    succ = None
    while root:
        if p.val < root.val:
            succ = root
            root = root.left
        else:
            root = root.right
    return succ

