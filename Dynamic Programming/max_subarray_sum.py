#__author__ = ritvikareddy2
#__date__ = 2019-03-23


def maxSubArray(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    if not nums:
        return 0
    localMax = nums[0]
    globalMax = nums[0]

    for i in range(1, len(nums)):
        localMax = max(localMax + nums[i], nums[i])
        globalMax = max(globalMax, localMax)
    return globalMax
