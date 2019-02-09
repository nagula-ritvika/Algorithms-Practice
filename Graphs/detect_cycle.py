#__author__ = ritvikareddy2
#__date__ = 2019-02-01

from collections import defaultdict


def has_cycle(graph):
    visited = defaultdict(lambda: False)
    recStack = defaultdict(lambda: False)

    for node in graph.keys():
        if not visited[node]:
            if hasCycleUtil(node, visited, recStack, graph):
                return True

    return False


def has_cycle_util(node, visited, recStack, graph):

    visited[node] = True
    recStack[node] = True

    for neighbor in graph[node]:
        if not visited[neighbor]:
            if has_cycle_util(neighbor, visited, recStack, graph):
                return True
            elif recStack[neighbor]:
                return True
    recStack[node] = False
    return False


if __name__ == '__main__':
    graph = {
        0: [2, 3],
        1: [0, 4],
        2: [4],
        3: [],
        4: []
    }
    print(has_cycle(graph))