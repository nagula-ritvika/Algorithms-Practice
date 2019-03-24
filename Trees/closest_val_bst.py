#__author__ = ritvikareddy2
#__date__ = 2019-03-23

def closestValue(root, target):
    """
    :type root: TreeNode
    :type target: float
    :rtype: int
    """
    closest = root.val
    while root:
        cur_diff = abs(root.val - target)
        closest_diff = abs(closest - target)
        if cur_diff < closest_diff:
            closest = root.val
        root = root.left if target < root.val else root.right
    return closest