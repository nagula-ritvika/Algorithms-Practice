class Node(object):
    def __init__(self, key, val):
        self.val = val
        self.next = None
        self.prev = None
        self.key = key


class LRUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capacity = capacity
        self.cache = {}
        self.head = Node(0, 0)
        self.tail = Node(0, 0)
        self.head.next = self.tail
        self.tail.prev = self.head

    def removeNode(self, node):
        # remove node from its curr location in dequeue
        node.prev.next = node.next
        node.next.prev = node.prev

    def addNodeAtHead(self, node):
        # add it to front of dequeue

        node.prev = self.head
        node.next = self.head.next
        self.head.next.prev = node
        self.head.next = node

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key in self.cache.keys():
            node = self.cache[key]
            self.removeNode(node)
            self.addNodeAtHead(node)
            return node.val

        return -1

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: void
        """
        if key in self.cache.keys():
            node = self.cache[key]
            self.removeNode(node)
        node = Node(key, value)
        self.addNodeAtHead(node)
        self.cache[key] = node

        if len(self.cache) > self.capacity:
            last = self.tail.prev
            self.removeNode(last)
            del self.cache[last.key]
            return last.val

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)


if __name__ == '__main__':
    cache = LRUCache(2)

    print(cache.put(1, 1))
    print(cache.put(2, 2))
    print(cache.get(1))
    # returns 1
    print(cache.put(3, 3))
    # evicts key 2
    print(cache.get(2))
    # returns - 1(not found)
    print(cache.put(4, 4))
    # evicts key 1
    print(cache.get(1))
    # returns - 1(not found)
    print(cache.get(3))
    # returns 3
    print(cache.get(4))
    # returns 4