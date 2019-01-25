#__author__ = ritvikareddy2
#__date__ = 2019-01-24

def selectionSort(arr):
    n = len(arr)
    for i in range(n):
        minIdx = i
        for j in range(i+1, n):
            if arr[minIdx] > arr[j]:
                minIdx = j
        temp = arr[minIdx]
        arr[minIdx] = arr[i]
        arr[i] = temp

    return arr


if __name__ == '__main__':
    A = [3, 45, 7, 8, 1]
    print(selectionSort(A))
