#__author__ = ritvikareddy2
#__date__ = 2019-01-24


def bubbleSort(arr):
    n = len(arr)

    for i in range(n):
        for j in range(n-i-1):
            if arr[j+1] < arr[j]:
                temp = arr[j]
                arr[j] = arr[j+1]
                arr[j+1] = temp

    return arr


if __name__ == '__main__':
    A = [3, 45, 7, 8, 1]
    print(bubbleSort(A))