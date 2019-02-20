#__author__ = ritvikareddy2
#__date__ = 2019-02-17


def updateBoard(board, click):
    """
    :type board: List[List[str]]
    :type click: List[int]
    :rtype: List[List[str]]
    """

    rows, cols = len(board), len(board[0])

    directions = [(0,1), (0,-1), (1,0), (-1,0), (1,1), (1, -1), (-1,1), (-1,-1)]
    click = tuple(click)
    stack = [click]
    seen = set([click])

    while stack:
        i, j = stack.pop()
        if board[i][j] == 'M':
            board[i][j] = 'X'


        else:
            # get number of mines adjacent to this cell
            mines_count = 0
            for r, c in directions:
                ni, nj = r + i, c + j
                if 0 <= ni < rows and 0 <= nj < cols and board[ni][nj] == 'M':
                    mines_count += 1

            if mines_count:
                board[i][j] = str(mines_count)

            else:
                board[i][j] = 'B'
                for r, c in directions:
                    ni, nj = r + i, c + j
                    if 0 <= ni < rows and 0 <= nj < cols and board[ni][nj] in ['M', 'E'] and (ni,
                                                                                              nj) not in \
                            seen:
                        stack.append((ni, nj))
                        seen.add((ni, nj))

    return board


if __name__ == '__main__':
    board = [["E", "E", "E", "E", "E"], ["E", "E", "M", "E", "E"], ["E", "E", "E", "E", "E"],
             ["E", "E", "E", "E", "E"]]
    click = [3, 0]
    print(updateBoard(board, click))

