#__author__ = ritvikareddy2
#__date__ = 2019-02-20


def lowestCommonAncestor(root, p, q):
    """
    :type root: TreeNode
    :type p: TreeNode
    :type q: TreeNode
    :rtype: TreeNode
    """
    if not root:
        return None
    curr = root
    while curr:

        if curr.val < p.val and curr.val < q.val:
            curr = curr.right
        elif curr.val > p.val and curr.val > q.val:
            curr = curr.left
        else:
            return curr
