#__author__ = ritvikareddy2
#__date__ = 2019-03-16


from collections import defaultdict


def groupAnagrams(strs):
    """
    :type strs: List[str]
    :rtype: List[List[str]]
    """
    res = defaultdict(list)
    for s in strs:
        # maintain count for each alphabet for every string
        counts = [0] * 26
        for c in s:
            counts[ord(c) - ord('a')] += 1
        res[tuple(counts)].append(s)

    return list(res.values())


if __name__ == '__main__':
    strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
    print(groupAnagrams(strs))

