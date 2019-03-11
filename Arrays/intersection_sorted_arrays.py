#__author__ = ritvikareddy2
#__date__ = 2019-03-11


def intersection_arrs(array1, array2):
    n = len(array1)
    m = len(array2)
    res = []

    p1, p2 = 0, 0

    while p1 < n and p2 < m:
        if array1[p1] == array2[p2]:
            res.append(array1[p1])
            p1 += 1
            p2 += 1
        elif array1[p1] < array2[p2]:
            p1 += 1
        else:
            p2 += 1

    return res


if __name__ == '__main__':
    array1 = [4, 5, 7, 7, 7, 8, 9]

    array2 = [4, 4, 4, 7, 7, 9, 10]

    print(intersection_arrs(array1, array2))