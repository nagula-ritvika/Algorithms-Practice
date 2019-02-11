#__author__ = ritvikareddy2
#__date__ = 2019-02-09


class Node:
    def __init__(self, val):
        self.left = None
        self.right = None
        self.val = val


def inorder_recursive(root):

    if root:
        inorder_recursive(root.left)
        print(root.val),
        inorder_recursive(root.right)


def inorder(root):
    if not root:
        return
    current = root
    stack = []
    flag = 0
    while not flag:
        if current:
            stack.append(current)
            current = current.left
        else:
            if stack:
                current = stack.pop()
                print(current.val)

                current = current.right
            else:
                break



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
