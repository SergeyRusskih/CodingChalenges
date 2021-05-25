def unique_path(m: int, n: int):
    dp = [ [ 0 for _ in range(n) ] for _ in range(m) ]
    dp[0][0] = 1

    for row in range(m):
        for cell in range(n):
            if row - 1 >= 0:
                dp[row][cell] += dp[row-1][cell]
            if cell - 1 >= 0:
                dp[row][cell] += dp[row][cell-1]

    return dp[m-1][n-1]

def test_5():
    result = unique_path(1, 3)
    assert result == 1

def test_1():
    result = unique_path(3, 7)
    assert result == 28

def test_2():
    result = unique_path(3, 2)
    assert result == 3

def test_3():
    result = unique_path(7, 3)
    assert result == 28

def test_4():
    result = unique_path(3, 3)
    assert result == 6