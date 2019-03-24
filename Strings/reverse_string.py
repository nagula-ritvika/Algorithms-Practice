#__author__ = ritvikareddy2
#__date__ = 2019-03-20


def reverse_string(s):
    # reverse in-place
    low = 0
    high = len(s) - 1
    while low <= high:
        x = s[low]
        s[low] = s[high]
        s[high] = x
        low += 1
        high -= 1
    return s
