#__author__ = ritvikareddy2
#__date__ = 2019-02-15


def reverseWords(s):
    """
    :type s: str
    :rtype: str
    """

    words = s.split(" ")
    reversed_s = ''
    for i in range(len(words) - 1, -1, -1):
        w = words[i].strip()
        if w:
            reversed_s += w + ' '

    return reversed_s.strip()
