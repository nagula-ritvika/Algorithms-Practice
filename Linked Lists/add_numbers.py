#__author__ = ritvikareddy2
#__date__ = 2019-02-16

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

def addTwoNumbers(l1, l2):
    """
    :type l1: ListNode
    :type l2: ListNode
    :rtype: ListNode
    """
    carry = 0
    x, y = 0, 0
    a, b = l1, l2
    head = ListNode(-1)
    curr = head
    while a is not None or b is not None:
        x = 0 if a is None else a.val
        y = 0 if b is None else b.val
        s = carry + x + y
        carry = s // 10
        s = s % 10
        curr.next = ListNode(s)
        curr = curr.next
        if a is not None:
            a = a.next
        if b is not None:
            b = b.next
    if carry > 0:
        curr.next = ListNode(carry)

    return head.next


if __name__ == '__main__':
    a = ListNode(2)
    a.next = ListNode(4)
    a.next.next = ListNode(3)

    b = ListNode(5)
    b.next = ListNode(6)
    b.next.next = ListNode(4)
    res = addTwoNumbers(a, b)
    sum = []
    while res != None:
        sum.append(res.val)
        res = res.next
    print(sum)
