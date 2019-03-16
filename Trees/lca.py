#__author__ = ritvikareddy2
#__date__ = 2019-02-20


class TreeNode(object):
    def __init__(self, x):
            self.val = x
            self.left = None
            self.right = None


def lowestCommonAncestor_iterative(root, p, q):

    if not root:
        return None

    if root.val == p or root.val == q:
        return root

    left = lowestCommonAncestor_iterative(root.left, p, q)
    right = lowestCommonAncestor_iterative(root.right, p, q)

    if left is not None and right is not None:
        return root.val
    elif left is not None:
        return root.left.val
    else:
        return root.right.val


def lowestCommonAncestor_recursive(root, p, q):
    """
    :type root: TreeNode
    :type p: TreeNode
    :type q: TreeNode
    :rtype: TreeNode
    """

    def lca_recur(node):
        if not node:
            return False

        left = lca_recur(node.left)
        right = lca_recur(node.right)

        curr = node == p or node == q

        if curr + left + right >= 2:
            global ans
            ans = node

        return curr or left or right

    lca_recur(root)
    return ans


def lca_ancestors(root, p, q):
    stack = [root]

    # Dictionary for parent pointers
    parent = {root: None}

    # Iterate until we find both the nodes p and q
    while p not in parent or q not in parent:

        node = stack.pop()

        # While traversing the tree, keep saving the parent pointers.
        if node.left:
            parent[node.left] = node
            stack.append(node.left)
        if node.right:
            parent[node.right] = node
            stack.append(node.right)

    # Ancestors set() for node p.
    ancestors = set()

    # Process all ancestors for node p using parent pointers.
    while p:
        ancestors.add(p)
        p = parent[p]

    # The first ancestor of q which appears in
    # p's ancestor set() is their lowest common ancestor.
    while q not in ancestors:
        q = parent[q]
    return q


if __name__ == '__main__':
    root = TreeNode(3)
    root.left = TreeNode(5)
    root.right = TreeNode(1)
    root.left.left = TreeNode(6)
    root.left.right = TreeNode(2)
    root.right.left = TreeNode(0)
    root.right.right = TreeNode(8)

    print(lowestCommonAncestor_iterative(root, 5, 1))