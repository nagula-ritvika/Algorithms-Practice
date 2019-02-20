#__author__ = ritvikareddy2
#__date__ = 2019-01-24


def find_fixed_point(arr, low, high):

    if low <= high:
        mid = (low + high)//2

    else:
        return -1

    if arr[mid] == mid:
        return mid

    elif arr[mid] > mid:
        return find_fixed_point(arr, low, mid - 1)
    else:
        return find_fixed_point(arr, mid + 1, high)


if __name__ == '__main__':
    inp = [-5, -1, 0, 3]
    print(find_fixed_point(inp, 0, len(inp)-1))
