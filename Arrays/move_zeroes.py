#__author__ = ritvikareddy2
#__date__ = 2019-02-19


def moveZeroes(nums):
    """
    :type nums: List[int]
    :rtype: void Do not return anything, modify nums in-place instead.
    """
    curr = 0
    for i in range(len(nums)):
        if nums[i] != 0:
            x = nums[i]
            nums[i] = nums[curr]
            nums[curr] = x
            curr += 1

    return nums


if __name__ == '__main__':
    print(moveZeroes([3, 4, 0, 10, 0, 9]))
