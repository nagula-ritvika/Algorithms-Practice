#__author__ = ritvikareddy2
#__date__ = 2019-02-20


def area(grid, r, c, visited):
    if not (0 <= r < len(grid) and 0 <= c < len(grid[0])) or (r, c) in visited or not grid[r][c]:
        return 0

    visited.add((r, c))

    return (1 + area(grid, r + 1, c, visited) + area(grid, r - 1, c, visited) + area(
        grid, r, c + 1, visited) + area(grid, r, c - 1, visited))


def maxAreaOfIsland(grid):
    """
    :type grid: List[List[int]]
    :rtype: int
    """
    visited = set()

    areas = []
    for r in range(len(grid)):
        for c in range(len(grid[0])):
            areas.append(area(grid, r, c, visited))

    return max(areas)

