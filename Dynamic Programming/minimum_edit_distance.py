#__author__ = ritvikareddy2
#__date__ = 2019-03-25


def min_edit_dist(s1, s2):
    m = len(s1)
    n = len(s2)

    dp_res = [[0]*(n+1) for i in range(m+1)]

    for i in range(m+1):
        for j in range(n+1):
            if i == 0:
                dp_res[i][j] = j
            elif j == 0:
                dp_res[i][j] = i
            elif s1[i-1] == s2[j-1]:
                dp_res[i][j] = dp_res[i-1][j-1]
            else:
                dp_res[i][j] = 1 + min(dp_res[i][j-1], dp_res[i-1][j-1], dp_res[i-1][j])

    return dp_res[-1][-1]


if __name__ == '__main__':
    str1 = "sunday"
    str2 = "saturday"
    print(min_edit_dist(str1, str2))