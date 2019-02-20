#__author__ = ritvikareddy2
#__date__ = 2019-01-24


def insertionSort(arr):
    n = len(arr)
    for i in range(1, n):
        curr = arr[i]
        j = i - 1
        while j >= 0 and curr < arr[j]:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = curr

    return arr


if __name__ == '__main__':
    A = [3, 45, 7, 8, 1]
    print(insertionSort(A))
