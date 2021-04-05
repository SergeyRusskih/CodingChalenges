def n_queen(n):
    
    sums = set()
    diffs = set()

    boards = []
    def dfs(row, board):
        if row == n:
            boards.append(list(board))
        
        for column in range(n):

            # https://www.geeksforgeeks.org/backtracking-introduction/
            if (column - row) not in diffs and (column + row) not in sums and column not in board:

                # apply value
                sums.add(column + row)
                diffs.add(column - row)
                board.append(column)

                # find solution
                dfs(row + 1, board)

                # remove value
                sums.remove(column + row)
                diffs.remove(column - row)
                board.pop()


    dfs(0, [])
    return [[ "." * column + "Q" + "." * (n-column-1) for column in board ] for board in boards ]

def test_3_queen():
    result = n_queen(3)
    assert result == []

def test_4_queen():
    result = n_queen(4)
    assert result == [
        [
            ".Q..",
            "...Q",
            "Q...",
            "..Q."
        ],
        [
            "..Q.",
            "Q...",
            "...Q",
            ".Q.."
        ]
    ]