#__author__ = ritvikareddy2
#__date__ = 2019-02-19


def sortArrayByParity(A):
    """
    :type A: List[int]
    :rtype: List[int]
    """
    left = 0
    right = len(A) - 1
    while left < right:
        if A[left] % 2 == 1 and A[right] % 2 == 0:
            x = A[left]
            A[left] = A[right]
            A[right] = x
        if A[left] % 2 == 0:
            left += 1
        if A[right] % 2 == 1:
            right -= 1

    return A