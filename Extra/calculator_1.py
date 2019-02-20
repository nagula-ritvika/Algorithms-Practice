#__author__ = ritvikareddy2
#__date__ = 2019-02-16


def calculate(s):
    """
    The expression string may contain open ( and closing parentheses ), the plus + or minus sign -,
    non-negative integers and empty spaces .
    :type s: str
    :rtype: int
    """
    res = 0
    stack = []
    num = 0
    sign = 1
    for i in s:
        if i.isdigit():
            num = 10*num + int(i)
        elif i in ['+', '-']:
            res += sign*num
            num = 0
            sign = -1 if i == '-' else 1
        elif i == '(':
            stack.append(res)
            stack.append(sign)
            sign = 1
            res = 0
        elif i == ')':
            res += sign*num
            res *= stack.pop()
            res += stack.pop()
            num = 0
    return res + sign*num


if __name__ == '__main__':
    print(calculate("1-(5)"))


