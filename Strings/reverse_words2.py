#__author__ = ritvikareddy2
#__date__ = 2019-02-16


def reverseWords(str):
    """
    :type str: List[str]
    :rtype: void Do not return anything, modify str in-place instead.
    """
    word_start = 0

    # reverse each word individually
    for i in range(len(str)):
        if str[i] == ' ':
            reverse_word(str, word_start, i - 1)
            word_start = i+1
        elif i == len(str) - 1:
            reverse_word(str, word_start, i)


    # reverse entire sentence
    reverse_word(str, 0, len(str)-1)


def reverse_word(s, start, end):
    # reverse in-place
    low = start
    high = end
    while low <= high:
        x = s[low]
        s[low] = s[high]
        s[high] = x
        low += 1
        high -= 1


if __name__ == '__main__':
    l = ["t", "h", "e", " ", "s", "k", "y", " ", "i", "s", " ", "b", "l", "u", "e"]
    reverseWords(l)
    print(l)
