#__author__ = ritvikareddy2
#__date__ = 2019-03-23

def sumNumbers(root):
    """
    :type root: TreeNode
    :rtype: int
    """
    if not root:
        return 0
    res = 0
    stack = [(root, root.val)]
    while stack:
        node, curSum = stack.pop()
        if node.right is None and node.left is None:
            res += curSum
        if node.left:
            stack.append((node.left, curSum * 10 + node.left.val))
        if node.right:
            stack.append((node.right, curSum * 10 + node.right.val))
    return res