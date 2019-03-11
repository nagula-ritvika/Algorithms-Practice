#__author__ = ritvikareddy2
#__date__ = 2019-02-20


class TreeNode(object):
    def __init__(self, x):
            self.val = x
            self.left = None
            self.right = None


class Solution:

    def kthSmallest(self, root, k):
        self.k = k
        self.res = None
        self.helper(root)
        return self.res

    def helper(self, node):
        if not node:
            return
        self.helper(node.left)
        self.k -= 1
        if self.k == 0:
            self.res = node.val
            return
        self.helper(node.right)


if __name__ == '__main__':
    root = TreeNode(3)
    root.left = TreeNode(1)
    root.right = TreeNode(4)
    root.left.right = TreeNode(2)
    s = Solution()
    print(s.kthSmallest(root, 1))
