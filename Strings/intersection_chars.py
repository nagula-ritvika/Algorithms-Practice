#__author__ = ritvikareddy2
#__date__ = 2019-03-11

from collections import defaultdict


def get_common_chars(arr1):
    chars_map = defaultdict(int)

    for letter in arr1[0]:
        chars_map[letter] += 1

    for word in arr1:
        temp = defaultdict(int)
        for letter in word:
            temp[letter] += 1

        for letter in chars_map.keys():
            chars_map[letter] = min(temp[letter], chars_map[letter])

    res = []

    for letter, c in chars_map.items():
        if c > 0:
            res.extend([letter] * c)

    return res


if __name__ == '__main__':
    print(get_common_chars(["bella", "label", "adelle", "illogical"]))