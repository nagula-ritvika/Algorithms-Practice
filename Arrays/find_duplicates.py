#__author__ = ritvikareddy2
#__date__ = 2019-02-20

def findDuplicates(nums):
    """
    :type nums: List[int]
    :rtype: List[int]
    """
    res = []
    if not nums:
        return res
    for i in range(len(nums)):
        idx = abs(nums[i]) - 1
        # print(idx)
        if nums[idx] < 0:
            res.append(abs(nums[i]))
        else:
            nums[idx] = -nums[idx]
    # print(nums)
    return res