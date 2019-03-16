#__author__ = ritvikareddy2
#__date__ = 2019-03-15


def get_number(res, ch):
    return 10*res + int(ch)


def perform_op(op, res, prev):

    if op == '*':
        return prev*res
    elif op == '/':
        if res != 0:
            return prev/res
        else:
            return 0


def eval_string(s):

    op = ''
    res = 0
    vals = []
    prev = 0
    ops = []
    flag = False

    for c in s:

        if c.isdigit():
            res = get_number(res, c)

        else:
            if flag:
                flag = False
                res = perform_op(op, res, prev)

            vals.append(res)
            res = 0

            if c == '*' or c == '/':
                prev = vals.pop()
                op = c
                flag = True
            else:
                ops.append(c)

    # handle last element operation
    vals.append(perform_op(op, res, prev))

    while len(vals) > 1:
        v1 = vals.pop()
        v2 = vals.pop()
        op = ops.pop()

        if op == '+':
            vals.append(v1+v2)
        elif op == '-':
            vals.append(v1-v2)

    return vals[0]


if __name__ == '__main__':
    print(eval_string("12+3*25"))


