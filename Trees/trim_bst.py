#__author__ = ritvikareddy2
#__date__ = 2019-02-18


class TreeNode(object):

    def __init__(self, x):
            self.val = x
            self.left = None
            self.right = None


def trimBST(root, L, R):
    """
    :type root: TreeNode
    :type L: int
    :type R: int
    :rtype: TreeNode
    """
    if not root:
        return None

    if root.val > R:
        return trimBST(root.left, L, R)
    if root.val < L:
        return trimBST(root.right, L, R)
    root.left = trimBST(root.left, L, R)
    root.right = trimBST(root.right, L, R)

    return root


if __name__ == '__main__':
    root = TreeNode(3)
    root.left = TreeNode(0)
    root.right = TreeNode(4)
    root.left.right = TreeNode(2)
    root.left.right.left = TreeNode(1)
    l = 1
    r = 3
    print(trimBST(root, l, r))
