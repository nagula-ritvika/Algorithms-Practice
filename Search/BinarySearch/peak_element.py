#__author__ = ritvikareddy2
#__date__ = 2019-01-24


def find_peak(arr, low, high, size):

    mid = (low + high)//2

    if (mid == 0 or arr[mid - 1] <= arr[mid]) and (mid == size - 1 or arr[mid + 1] <= arr[mid]):
        return arr[mid]
    elif mid > 0 and arr[mid - 1] > arr[mid]:
        return find_peak(arr, low, mid - 1, size)
    else:
        return find_peak(arr, mid + 1, high, size)


if __name__ == '__main__':
    inp = [1, 5, 4, 3, 2]
    print(find_peak(inp, 0, len(inp) - 1, len(inp)))
