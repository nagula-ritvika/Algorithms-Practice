#__author__ = ritvikareddy2
#__date__ = 2019-02-20

import collections


def findCircleNum(M):
    """
    :type M: List[List[int]]
    :rtype: int
    """
    visited = collections.defaultdict(lambda: False)
    count = 0
    queue = []

    for i in range(len(M)):
        if not visited[i]:
            queue.append(i)

            while queue:
                curr = queue.pop(0)
                visited[curr] = True
                # get all friends/neighbors of curr node and append to queue
                for j in range(len(M)):
                    if M[curr][j] and not visited[j]:
                        queue.append(j)
            # queue is empty implies we have traversed one friends circle, so
            # increment count
            count += 1
    return count
