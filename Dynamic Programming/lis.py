#__author__ = ritvikareddy2
#__date__ = 2019-03-25


def lis(arr):

    lis = [1] * len(arr)

    for i in range(1, len(arr)):
        for j in range(0, i):
            if arr[j] < arr[i] and lis[i] < lis[j] + 1:
                lis[i] = 1 + lis[j]

    return max(lis)


if __name__ == '__main__':
    arr = [10, 22, 9, 33, 21, 50, 41, 60]
    print(lis(arr))
