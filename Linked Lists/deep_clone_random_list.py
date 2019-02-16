#__author__ = ritvikareddy2
#__date__ = 2019-02-15


# Definition for singly-linked list with a random pointer.
class RandomListNode(object):
    def __init__(self, x):
        self.label = x
        self.next = None
        self.random = None


class IterativeSolution(object):
    def __init__(self):
        self.visited = {}

    def makeCopy(self, node):

        if node:
            if node not in self.visited.keys():
                self.visited[node] = RandomListNode(node.label)
            return self.visited[node]
        return None

    def copyRandomList(self, head):
        """
        :type head: RandomListNode
        :rtype: RandomListNode
        """

        if not head:
            return head

        old_head = head
        new_head = RandomListNode(old_head.label)
        self.visited[old_head] = new_head

        while old_head:
            new_head.next = self.makeCopy(old_head.next)
            new_head.random = self.makeCopy(old_head.random)

            old_head = old_head.next
            new_head = new_head.next

        return self.visited[head]


class OptimizedSpaceSolution(object):

    def copyRandomList(self, head):
        """
        :type head: RandomListNode
        :rtype: RandomListNode
        """

        if not head:
            return head

        # make clones with next pointers set and add them adjacent to corresponding original nodes
        cur = head
        while cur:
            new_cur = RandomListNode(cur.label)
            new_cur.next = cur.next
            cur.next = new_cur
            cur = new_cur.next

        # copy random pointers of clones into clones made above
        cur = head
        while cur:

            cur_clone = cur.next
            cur_clone.random = cur.random.next if cur.random else None
            cur = cur_clone.next

        # separate clones and originals in mixed linked list
        old_cur = head
        new_cur = head.next
        new_head = head.next

        while old_cur:

            old_cur.next = new_cur.next
            new_cur.next = new_cur.next.next if new_cur.next else None

            old_cur = old_cur.next
            new_cur = new_cur.next

        return new_head


