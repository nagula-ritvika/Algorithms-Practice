#__author__ = ritvikareddy2
#__date__ = 2019-03-08

# !/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'kthPerson' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER k
#  2. INTEGER_ARRAY p
#  3. INTEGER_ARRAY q
#

def kthPerson(k, p, q):
    # Write your code here
    answer = []

    for qi in q:
        res = []

        # print(idx)
        for i in range(len(p)):
            pi = p[i]
            if pi >= qi and len(res) < k:
                res.append(i + 1)
            if len(res) == k:
                break
        if len(res) < k:
            answer.append(0)
        else:
            answer.append(res[-1])
        # print(res)
    return answer

