#__author__ = ritvikareddy2
#__date__ = 2019-01-24


def find_pivot_bitonic(arr, low, high):

    if low == high:
        return arr[low]

    if low + 1 == high:
        return arr[low] if arr[low] > arr[high] else arr[high]

    mid = (low + high)//2

    if arr[mid-1] < arr[mid] and arr[mid] > arr[mid + 1]:
        return arr[mid]
    elif arr[mid - 1] < arr[mid] and arr[mid] < arr[mid + 1]:
        return find_pivot_bitonic(arr, mid + 1, high)
    else:
        return find_pivot_bitonic(arr, low, mid - 1)


if __name__ == '__main__':

    inp = [1, 5, 7, 9, 6, 2]
    print(find_pivot_bitonic(inp, 0, len(inp) - 1))


