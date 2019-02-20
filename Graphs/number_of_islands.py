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

