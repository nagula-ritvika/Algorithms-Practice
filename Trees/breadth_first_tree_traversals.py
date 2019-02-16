#__author__ = ritvikareddy2
#__date__ = 2019-02-09


class Node:
    def __init__(self, val):
        self.left = None
        self.right = None
        self.val = val


def level_order_traversal(root):

    if not root:
        return

    queue = [root]

    while queue:
        current = queue.pop(0)
        print(current.val)

        if current.left:
            queue.append(current.left)

        if current.right:
            queue.append(current.right)


def level_order_traversal_with_level(root):
    if not root:
        return

    queue = [root]
    path = []
    while queue:
        count = len(queue)
        level = []
        while count > 0:

            current = queue.pop(0)
            level.append(current.val)

            if current.left:
                queue.append(current.left)

            if current.right:
                queue.append(current.right)
            count -= 1
        path.append(level)
    print(path)

