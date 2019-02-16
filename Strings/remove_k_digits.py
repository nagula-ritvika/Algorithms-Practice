#__author__ = ritvikareddy2
#__date__ = 2019-02-15


def handleLeadingZeroes(s):
    while s[0] == "0" and len(s) > 1:
        s = s[1:]
    return s


def removeKdigits(num, k):
    """
    :type num: str
    :type k: int
    :rtype: str
    """
    if k == len(num):
        return "0"

    stack = []
    for i in range(len(num)):
        while k > 0 and len(stack) > 0 and stack[-1] > num[i]:
            stack.pop()
            k -= 1
        stack.append(num[i])

    # handle all equal or increasing numbers
    # stack = stack[0:len(stack)-k]
    while k > 0:
        stack.pop()
        k -= 1

    new_num = ''.join(stack)
    new_num = handleLeadingZeroes(new_num)

    return new_num


if __name__ == '__main__':
    n = "87"
    k = 2
    print(removeKdigits(n, k))