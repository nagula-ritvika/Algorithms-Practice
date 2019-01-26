#__author__ = ritvikareddy2
#__date__ = 2019-01-25


def find_floor(arr, x, low, high):

    if x < arr[low]:
        return -1

    if arr[high] <= x:
        return arr[high]

    mid = (low + high)//2

    if low == mid:
        return arr[low]

    if arr[mid] == x:
        return arr[mid]

    if arr[mid] < x:
        return find_floor(arr, x, mid, high)
    else:
        return find_floor(arr, x, low, mid - 1)


if __name__ == '__main__':

    inp = [1, 5, 9, 11, 15]
    print(find_floor(inp, -2, 0, len(inp) - 1))
