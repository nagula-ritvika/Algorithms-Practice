#__author__ = ritvikareddy2
#__date__ = 2019-02-15


def handleLeadingZeroes(s):

    while s[0] == "0" and len(s) > 1:
        s = s[1:]
    return s


def compareVersion(version1, version2):
    """
    :type version1: str
    :type version2: str
    :rtype: int
    """
    v1 = version1.split(".")
    v2 = version2.split(".")

    len_diff = len(v1) - len(v2)
    n = len(v1) if len_diff > 0 else len(v2)

    if len_diff < 0:
        v1 += ["0"] * abs(len_diff)
    elif len_diff > 0:
        v2 += ["0"] * len_diff

    for i in range(n):

        v1[i] = int(handleLeadingZeroes(v1[i]))
        v2[i] = int(handleLeadingZeroes(v2[i]))

        if v1[i] > v2[i]:
            return 1
        elif v1[i] < v2[i]:
            return -1
        elif i == n-1 and v1[i] == v2[i]:
            return 0


if __name__ == '__main__':
    v1 = "01"
    v2 = "1"
    print(compareVersion(v1, v2))
