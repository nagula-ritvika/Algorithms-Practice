#__author__ = ritvikareddy2
#__date__ = 2019-03-12


# O(n+m) solution
def kth_element(arr1, arr2, k):

    res = []

    p1 = 0
    p2 = 0

    while p1 < len(arr1) and p2 < len(arr2):

        if arr1[p1] < arr2[p2]:
            res.append(arr1[p1])
            p1 += 1
        else:
            res.append(arr2[p2])
            p2 += 1
        if len(res) == k:
            return res[-1]

    while p1 < len(arr1):
        res.append(arr1[p1])
        p1 += 1
        if len(res) == k:
            return res[-1]

    while p2 < len(arr2):
        res.append(arr1[p2])
        p2 += 1
        if len(res) == k:
            return res[-1]


def efficient_kth_element(arr1, arr2, k):

    if k >= len(arr1) + len(arr2):
        return -1
    k -= 1
    while k > 0:
        mid = (k-1)//2
        if mid >= len(arr1) or arr2[mid] <= arr1[mid]:
            arr2 = arr2[mid+1:]
        elif mid >= len(arr2) or arr1[mid] <= arr2[mid]:
            arr1 = arr1[mid+1:]
        # else:

        k -= mid + 1

    if len(arr1) == 0:
        return arr2[0]
    if len(arr2) == 0:
        return arr1[0]
    return min(arr1[0], arr2[0])


if __name__ == '__main__':
    a = [2, 3, 6, 7, 9]
    b = [1, 4, 8, 10]
    print(kth_element(a, b, 5))
    print(efficient_kth_element(a, b, 5))



