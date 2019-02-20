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


def iter_find_peak(A):
    low = 0
    high = len(A) - 1

    while low <= high:
        mid = low + (high - low) // 2

        left_idx = mid - 1
        right_idx = mid + 1

        left = -float('inf') if left_idx < 0 else A[left_idx]
        right = -float('inf') if right_idx >= len(A) else A[right_idx]
        cur = A[mid]

        if cur >= left and cur >= right:
            return mid

        elif left > cur:
            high = mid - 1
        else:
            low = mid + 1

    return -1


if __name__ == '__main__':
    inp = [1, 5, 4, 3, 2]
    print(find_peak(inp, 0, len(inp) - 1, len(inp)))
    a = [18, 29, 38, 59, 98, 100, 99, 98, 90]
    print(iter_find_peak(a))
