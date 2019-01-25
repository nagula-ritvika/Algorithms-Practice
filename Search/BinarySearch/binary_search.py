#__author__ = ritvikareddy2
#__date__ = 2019-01-24


def binary_search(x, arr, low, high):

    if low <= high:
        mid = (low+high)//2
    else:
        return -1

    if arr[mid] == x:
        return arr[mid]
    elif x < arr[mid]:
        return binary_search(x, arr, low, mid-1)
    elif x > arr[mid]:
        return binary_search(x, arr, mid+1, high)


if __name__ == '__main__':
    arr = [1, 3, 5, 7, 8]

    print(binary_search(4, arr, 0, len(arr)-1))
