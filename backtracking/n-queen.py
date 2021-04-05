def n_queen(n):
    
    sums = set()
    diffs = set()

    def dfs(row, result):
        if row == n:
            return result
        
        for column in range(n):

            # https://www.geeksforgeeks.org/backtracking-introduction/
            if (column - row) not in diffs and (column + row) not in sums and column not in result:

                # apply value
                sums.add(column + row)
                diffs.add(column - row)
                result.append(column)

                # find solution
                board = dfs(row + 1, result)
                if board:
                    return board

                # remove value
                sums.remove(column + row)
                diffs.remove(column - row)
                result.pop()

        return None


    result = []
    dfs(0, result)
    return [ "." * column + "Q" + "." * (n-column-1) for column in result ]

def test_3_queen():
    result = n_queen(3)
    assert result == []

def test_4_queen():
    result = n_queen(4)
    assert result == [
        '.Q..',
        '...Q',
        'Q...',
        '..Q. '
    ]