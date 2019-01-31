#__author__ = ritvikareddy2
#__date__ = 2019-01-31

from collections import defaultdict


def dfs(source, graph):

    path = []
    visited = defaultdict(lambda: False)

    stack = [source]

    while stack:

        current = stack.pop()

        if not visited[current]:
            visited[current] = True
            path.append(current)

        for neighbor in graph[current]:
            if not visited[neighbor]:
                stack.append(neighbor)

    return path


if __name__ == '__main__':
    g = {
        0: [2, 3],
        1: [0, 4],
        2: [1],
        3: [],
        4: []
    }

    print(dfs(2, g))
