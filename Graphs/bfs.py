#__author__ = ritvikareddy2
#__date__ = 2019-01-31

from collections import defaultdict


def bfs(source, graph):

    visited = defaultdict(lambda: False)
    path = []

    queue = [source]
    visited[source] = True

    while queue:

        current = queue.pop(0)
        path.append(current)

        for neighbor in graph[current]:
            if not visited[neighbor]:
                queue.append(neighbor)
                visited[neighbor] = True

    return path


if __name__ == '__main__':
    g = {
        0: [1, 2],
        1: [2],
        2: [0, 3],
        3: [3]

    }

    print(bfs(2, g))
