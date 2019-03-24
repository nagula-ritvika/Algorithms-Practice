#__author__ = ritvikareddy2
#__date__ = 2019-03-20

from collections import defaultdict


def maxSubArrayLen(nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: int
    """
    curr_sum = 0
    max_i = 0
    sums = defaultdict(lambda: -1)
    sums[0] = -1

    for i in range(len(nums)):
        curr_sum += nums[i]
        if curr_sum not in sums:
            sums[curr_sum] = i
        if curr_sum - k in sums:
            max_i = max(max_i, i - sums[curr_sum - k])

    return max_i


if __name__ == '__main__':
    nums = [1, -1, 5, -2, 3, 0]
    k = 3
    print(maxSubArrayLen(nums, k))
