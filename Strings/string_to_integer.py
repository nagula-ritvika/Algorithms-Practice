#__author__ = ritvikareddy2
#__date__ = 2019-02-17

def myAtoi(str):
    """
    :type str: str
    :rtype: int
    """
    res = ''
    sign = 0
    for s in str:
        if s != ' ':
            if s != '+' and s != '-' and not s.isdigit():
                return 0
            elif s in ['+', '-'] and not sign:
                sign = 1
                res += s
            else:

                res += s
    if res in ['+', '-', '']:
        return 0
    if int(res) > 2 ** 31:
        return 2 ** 31 - 1
    elif int(res) < -2 ** 31:
        return -2 ** 31
    else:
        return int(res)

if __name__ == '__main__':
    s = '+-2'
    print(myAtoi(s))
