#__author__ = ritvikareddy2
#__date__ = 2019-03-11

def spiralOrder(matrix):
    """
    :type matrix: List[List[int]]
    :rtype: List[int]
    """

    if not matrix:
        return []

    res = []
    r1, c1, r2, c2 = 0, 0, len(matrix)-1, len(matrix[0])-1

    while r1 <= r2 and c1 <= c2:
        # top boundary
        for c in range(c1, c2+1):
            res.append(matrix[r1][c])

        # right boundary
        for r in range(r1+1, r2+1):
            res.append(matrix[r][c2])

        # bottom boundary
        for c in range(c2-1, c1, -1):
            res.append(matrix[r2][c])

        # left boundary
        for r in range(r2, r1, -1):
            res.append(matrix[r][c1])

        r1 += 1
        c1 += 1
        r2 -= 1
        c2 -= 1


    return res


if __name__ == '__main__':
    matrix = [
        [1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 10, 11, 12]
    ]
    print(spiralOrder(matrix))
