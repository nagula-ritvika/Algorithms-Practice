#__author__ = ritvikareddy2
#__date__ = 2019-02-20


def frequencySort(s):
    """
    :type s: str
    :rtype: str
    """
    counter = {}
    for c in s:
        counter[c] = 1 if c not in counter else counter[c] + 1

    sorted_counter = sorted(counter.items(), key=lambda x: x[1], reverse=True)
    res = ''
    for k, v in sorted_counter:
        res += k * v
    return res
