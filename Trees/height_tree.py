#__author__ = ritvikareddy2
#__date__ = 2019-02-11


class Node:
    def __init__(self, val):
        self.left = None
        self.right = None
        self.val = val


def get_height(root):
    if not root:
        return 0
    left_ht = get_height(root.left)
    right_ht = get_height(root.right)

    if left_ht > right_ht:
        return 1 + get_height(root.left)
    else:
        return 1 + get_height(root.right)
