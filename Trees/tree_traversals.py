#__author__ = ritvikareddy2
#__date__ = 2019-02-09


class Node:
    def __init__(self, val):
        self.left = None
        self.right = None
        self.val = val


def inorder(root):

    if root:
        inorder(root.left)
        print(root.val),
        inorder(root.right)


def preorder(root):
    if root:
        print(root.val),
        preorder(root.left)
        preorder(root.right)


def postorder(root):
    if root:
        postorder(root.left)
        postorder(root.right)
        print(root.val),
