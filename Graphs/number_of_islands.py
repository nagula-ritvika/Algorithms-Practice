#__author__ = ritvikareddy2
#__date__ = 2019-02-20


def dfs(grid, r, c):
    rows = len(grid)
    cols = len(grid[0])

    if r < 0 or c < 0 or r >= rows or c >= cols or grid[r][c] == '0':
        return

    grid[r][c] = '0'
    dfs(grid, r + 1, c)
    dfs(grid, r - 1, c)
    dfs(grid, r, c + 1)
    dfs(grid, r, c - 1)


def numIslands(grid):
    """
    :type grid: List[List[str]]
    :rtype: int
    """
    if not grid:
        return 0

    rows = len(grid)
    cols = len(grid[0])

    islands = 0

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == '1':
                islands += 1
                dfs(grid, r, c)

    return islands

# without using visited
class Solution(object):
    def area(self, grid, r, c):

        if not (0 <= r < len(grid) and 0 <= c < len(grid[0])) or not grid[r][c]:
            return 0

        grid[r][c] = 0

        return (1 + self.area(grid, r + 1, c) + self.area(grid, r - 1, c) + self.area(grid, r,
                                                                                      c + 1) + self.area(
            grid, r, c - 1))

    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """

        areas = []
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                areas.append(self.area(grid, r, c))

        return max(areas)