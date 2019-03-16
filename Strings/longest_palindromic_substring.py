#__author__ = ritvikareddy2
#__date__ = 2019-03-12


def isPalindrome(p):
    return p == reversed(p)


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










