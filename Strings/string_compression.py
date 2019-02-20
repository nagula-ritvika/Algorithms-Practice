#__author__ = ritvikareddy2
#__date__ = 2019-02-20


def compress(chars):
    """
    :type chars: List[str]
    :rtype: int
    """
    i = 0
    count = 1
    j = 1
    while j < len(chars):
        if chars[i] == chars[j]:
            j += 1
            count += 1
        else:
            i += 1
            chars[i] = count
            count = 1
            i += 1
    return chars[:i + 1]


if __name__ == '__main__':
    print(compress(["a", "a", "b", "b", "c", "c", "c"]))
