#__author__ = ritvikareddy2
#__date__ = 2019-02-20


# finding product and diving by total product fails when 0s are present in the array

def productExceptSelf(nums):
    """
    :type nums: List[int]
    :rtype: List[int]
    """
    prod = 1
    res = [1] * len(nums)
    for i in range(len(nums)):
        res[i] *= prod
        prod *= nums[i]
    prod = 1
    for i in range(len(nums) - 1, -1, -1):
        res[i] *= prod
        prod *= nums[i]

    return res


if __name__ == '__main__':
    print(productExceptSelf([1, 2, 3, 4]))
