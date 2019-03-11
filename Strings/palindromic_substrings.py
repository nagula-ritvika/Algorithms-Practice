#__author__ = ritvikareddy2
#__date__ = 2019-02-20


def manachers(s):
    a = '@#' + '#'.join(s) + '#$'
    z = [0] * len(a)
    center = right = 0

    for i in range(1, len(a) - 1):
        if i < right:
            z[i] = min(right - i, z[2 * center - i])

        while a[i + z[i] + 1] == a[i - z[i] - 1]:
            z[i] += 1
        if i + z[i] > right:
            center, right = i, i + z[i]

    return z


def countSubstrings(s):
    """
    :type s: str
    :rtype: int
    """
    return sum((v + 1) // 2 for v in manachers(s))


if __name__ == '__main__':
    print(countSubstrings("aaa"))
