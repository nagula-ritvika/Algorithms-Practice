#__author__ = ritvikareddy2
#__date__ = 2019-02-15


class Node:
    def __init__(self, val):
        self.left = None
        self.right = None
        self.val = val


def zigzagLevelOrder(root):
    """
    :type root: TreeNode
    :rtype: List[List[int]]
    """
    if not root:
        return

    queue = [root]
    path = []
    flag = 0

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

        level = level if not flag else level[::-1]
        flag = not flag
        path.append(level)

    return path


if __name__ == '__main__':
    input = {3: [9, 20], 20: [15, 7]}
    root = Node(3)
    root.left = Node(9)
    root.right = Node(20)
    root.right.left = Node(15)
    root.right.right = Node(7)
    print(zigzagLevelOrder(root))


