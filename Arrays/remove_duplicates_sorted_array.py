#__author__ = ritvikareddy2
#__date__ = 2019-02-20


def removeDuplicates(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    if not nums:
        return 0
    i = 0
    j = 1
    while j < len(nums):
        if nums[i] == nums[j]:
            j += 1
        else:
            i += 1
            nums[i] = nums[j]
    return nums[:i + 1]
