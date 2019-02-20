#__author__ = ritvikareddy2
#__date__ = 2019-02-18


def decodeString(s):
    """
    :type s: str
    :rtype: str
    """
    k = 0
    res = ''
    stack = []
    for i in s:
        if i.isdigit():
            k = 10 * k + int(i)
        elif i == '[':
            stack.append(res)
            stack.append(k)
            res = ''
            k = 0
        elif i == ']':
            num = stack.pop()
            x = stack.pop()
            res = x + num * res
        else:
            res += i

    return res


if __name__ == '__main__':
    s = "3[a]2[bc]"
    print(decodeString(s))
