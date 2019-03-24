#__author__ = ritvikareddy2
#__date__ = 2019-03-12


def expand_str(s, left, right):

    while left >= 0 and right <= len(s) - 1 and s[left] == s[right]:
        left -= 1
        right += 1

    return s[left+1:right]


def modified_longestPalindrome(s):

    res = ""

    for i in range(len(s)):
        odd_p = expand_str(s, i, i+1)
        res = odd_p if len(odd_p) > len(res) else res
        even_p = expand_str(s, i, i)
        res = even_p if len(even_p) > len(res) else res

    return res


def longestPlaindrome(s):
    longest = ''
    i = 1

    # new_s = '_' + '_'.join(list(s)) + '_'

    while i < len(s):

        # odd length palindromes
        left = i - 1
        right = i + 1

        while left >= 0 and right <= len(s) - 1:
            if s[left] == s[right]:
                curr = s[left:right + 1]
                if len(curr) > len(longest):
                    longest = curr
                left -= 1
                right += 1
            else:
                break

        # even length palindromes
        left = i - 1
        right = i

        while left >= 0 and right <= len(s) - 1:
            if s[left] == s[right]:
                curr = s[left:right + 1]
                if len(curr) >= len(longest):
                    longest = curr
                left -= 1
                right += 1
            else:
                break

        i += 1

    return longest


if __name__ == '__main__':

    print(longestPlaindrome('abba'))

    print(modified_longestPalindrome('abba'))

    print(modified_longestPalindrome('bab'))










