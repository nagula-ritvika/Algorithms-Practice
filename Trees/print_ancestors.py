#__author__ = ritvikareddy2
#__date__ = 2019-02-11


class Node:
    def __init__(self, val):
        self.left = None
        self.right = None
        self.val = val


def print_all_ancestors(root, node_val):

    if not root:
        return False

    if root.val == node_val:
        return True

    if print_all_ancestors(root.left, node_val) or print_all_ancestors(root.right, node_val):
        print(root.val)
        return True

    return False
