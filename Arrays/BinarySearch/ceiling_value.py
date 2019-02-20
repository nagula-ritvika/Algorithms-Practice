# __author__ = ritvikareddy2
# __date__ = 2019-01-25


def find_ceil(arr, x, low, high):

    if arr[high] < x:
        return -1

    if arr[low] >= x:
        return arr[low]

    mid = (low + high) // 2

    if high == mid:
        return arr[high]

    if arr[mid] == x:
        return arr[mid]

    if arr[mid] < x:
        return find_ceil(arr, x, mid + 1, high)
    else:
        return find_ceil(arr, x, low, mid)


if __name__ == '__main__':
    inp = [1, 5, 9, 11, 15, 22]
    print(find_ceil(inp, 24, 0, len(inp) - 1))
