#__author__ = ritvikareddy2
#__date__ = 2019-03-16


from collections import defaultdict

def canFinish(numCourses, prerequisites):
    """
    :type numCourses: int
    :type prerequisites: List[List[int]]
    :rtype: bool
    """

    graph = defaultdict(list)
    # 0: not visited, -1: currently visiting, 1: visited
    visited = defaultdict(lambda: 0)

    for i, j in prerequisites:
        graph[i].append(j)


    def dfs(node):
        if visited[node] == -1:
            # cycle exists
            return False
        if visited[node] == 1:
            # prereq finished before
            return True
        # not visited this node before
        visited[node] = -1
        for neighbor in graph[node]:
            if not dfs(neighbor):
                return False
        visited[node] = 1
        return True

    for node in graph.keys():
        if not dfs(node):
            return False

    return True


