#__author__ = ritvikareddy2
#__date__ = 2019-02-20


def wallsAndGates(rooms):
    """
    :type rooms: List[List[int]]
    :rtype: void Do not return anything, modify rooms in-place instead.
    """
    dirs = [(-1, 0), (1, 0), (0, 1), (0, -1)]
    empty = 2 ** 30

    m = len(rooms)

    if not m:
        return

    n = len(rooms[0])

    queue = []
    for r in range(m):
        for c in range(n):
            if rooms[r][c] == 0:
                queue.append((r, c))

    while queue:
        r, c = queue.pop(0)
        for d in dirs:
            nr = r + d[0]
            nc = c + d[1]

            if not (0 <= nr < m and 0 <= nc < n) or rooms[nr][nc] <= empty:
                continue
            rooms[nr][nc] = rooms[r][c] + 1
            queue.append((nr, nc))
