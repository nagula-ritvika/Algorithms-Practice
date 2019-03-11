#__author__ = ritvikareddy2
#__date__ = 2019-02-26


from functools import reduce

import sys
import random

import requests
# from bs4 import BeautifulSoup


def find_fav_num():
    uid = "remeeting"
    pwd = "quiz"
    endpoint_url = "https://remeeting.com/quiz/python_script.cgi?number="

    for i in range(100, 1000):
        page = requests.get(endpoint_url+str(i), auth=(uid, pwd)).content
        soup = BeautifulSoup(page, 'html.parser')
        if 'Sorry' not in soup.text:
            print(i)
            break




def function(data):
    ss, s, n = reduce(lambda a, b: map(sum, zip(a, b)), [(x * x, x, 1) for x in data])
    return (ss - s * s / n) / n

def refactored(data):
    if not data:
        return 0
    n = len(data)
    s = sum(data)
    ss = sum([x*x for x in data])

    return ss/n - (s*s)/(n*n)


def process():
    count = 1
    for line in sys.stdin:
        rndom_num = random.randint(0,9)
        sys.stdout.write(str(rndom_num))
        if count == 10:
            sys.stderr.write(line)
            count = 0
        count += 1


if __name__ == '__main__':
    data = [1,2,4]
    data = []
    # print(function(data))
    # print(refactored(data))
    process()
    # find_fav_num()