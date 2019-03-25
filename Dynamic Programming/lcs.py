#__author__ = ritvikareddy2
#__date__ = 2019-03-25


def lcs(s1, s2):
    m = len(s1)
    n = len(s2)

    lcs = [[None]*(n+1) for i in range(m+1)]

    for i in range(m+1):
        for j in range(n+1):
            if i == 0 or j == 0:
                lcs[i][j] = 0
            elif s1[i-1] == s2[j-1]:
                lcs[i][j] = lcs[i-1][j-1] + 1
            else:
                lcs[i][j] = max(lcs[i][j-1], lcs[i-1][j])

    return lcs[-1][-1]


if __name__ == '__main__':
    X = "AGGTAB"
    Y = "GXTXAYB"
    print(lcs(X, Y))

