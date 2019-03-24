#__author__ = ritvikareddy2
#__date__ = 2019-03-16


def trap_pointers(height):
    """
    :type height: List[int]
    :rtype: int
    """

    if not height:
        return 0

    res = 0
    left = 0
    right = len(height) - 1
    left_max = 0
    right_max = 0

    while left < right:

        if height[left] < height[right]:
            if height[left] >= left_max:
                left_max = height[left]

            else:
                res += left_max - height[left]
            left += 1

        else:
            if height[right] >= right_max:
                right_max = height[right]
            else:
                res += right_max - height[right]
            right -= 1

    return res


def trap_dp(height):
    """
    :type height: List[int]
    :rtype: int
    """

    if not height:
        return 0

    res = 0
    left_max = [0] * len(height)
    right_max = [0] * len(height)

    left_max[0] = height[0]
    for i in range(1, len(height)):
        left_max[i] = max(height[i], left_max[i-1])

    right_max[-1] = height[-1]
    for i in range(len(height)-2, -1, -1):
        right_max[i] = max(height[i], right_max[i+1])

    for i in range(1, len(height)):
        res += min(left_max[i], right_max[i]) - height[i]

    return res


if __name__ == '__main__':
    h = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
    print(trap_dp(h))
    print(trap_pointers(h))