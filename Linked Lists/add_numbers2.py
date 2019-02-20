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
    a = []
    b = []
    a_head = l1
    b_head = l2
    while a_head is not None:
        a.append(a_head.val)
        a_head = a_head.next
    while b_head is not None:
        b.append(b_head.val)
        b_head = b_head.next


    head = ListNode(-1)
    carry = 0
    while a or b or carry:
        s = (a.pop() if a else 0) + (b.pop() if b else 0) + carry
        carry = s//10
        s = s%10
        curr = ListNode(s)
        curr.next = head.next
        head.next = curr

    return head.next



