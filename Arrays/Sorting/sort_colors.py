#__author__ = ritvikareddy2
#__date__ = 2019-02-16


def sortColors(nums):
    """
    Given an array with n objects colored red, white or blue, sort them in-place so that objects
    of the same color are adjacent, with the colors in the order red, white and blue.
    Here, we will use the integers 0, 1, and 2 to represent the color red, white, and blue respectively.
    :type nums: List[int]
    :rtype: void Do not return anything, modify nums in-place instead.
    """

    red, white, blue = 0, 0, len(nums) - 1

    while white <= blue:

        # if there is red in white's place
        if nums[white] == 0:
            nums[white], nums[red] = nums[red], nums[white]
            white += 1
            red += 1
        elif nums[white] == 1:
            white += 1
        else:
            nums[white], nums[blue] = nums[blue], nums[white]
            blue -= 1

    return nums


if __name__ == '__main__':
    print(sortColors([1, 2, 0]))
