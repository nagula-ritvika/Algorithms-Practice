#__author__ = ritvikareddy2
#__date__ = 2019-02-18

def calculate(s):
    """
    The expression string contains only non-negative integers, +, -, *, / operators and empty
    spaces. The integer division should truncate toward zero.

    :type s: str
    :rtype: int
    """
    if not s:
        return 0

    stack = []
    num = 0
    sign = "+"

    for i in range(len(s)):
        curr = s[i]
        if curr.isdigit():
            num = 10 * num + int(curr)
        if not curr.isdigit() and curr != ' ' or i == len(s) - 1:
            if sign == '-':
                stack.append(-num)
            elif sign == '+':
                stack.append(num)
            elif sign == '*':
                stack.append(stack.pop()*num)
            elif sign == '/':
                x = stack.pop()
                if x//num < 0 and x%num != 0:
                    stack.append(x//num + 1)
                else:
                    stack.append(x//num)
            sign = curr
            num = 0

    return sum(stack)


if __name__ == '__main__':
    s = "14-3/2"
    print(calculate(s))
