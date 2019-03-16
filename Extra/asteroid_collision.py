#__author__ = ritvikareddy2
#__date__ = 2019-03-15


def asteroidCollision(asteroids):
    """
    :type asteroids: List[int]
    :rtype: List[int]
    """

    stack = []
    for next in asteroids:
        while stack and next < 0 < stack[-1]:
            # next remains and top of stack explodes
            if abs(next) > abs(stack[-1]):
                stack.pop()
                continue
            # both explode
            elif abs(next) == abs(stack[-1]):
                stack.pop()
            break
        else:
            stack.append(next)
    return stack


if __name__ == '__main__':
    print(asteroidCollision([5, 10, -15, 1]))





