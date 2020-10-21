import queue as queue

def num_of_islands(grid):
    count = 0
    grid_len = len(grid)
    row_len = len(grid[0])
    for i in range(grid_len):
        for j in range(row_len):
            if grid[i][j] == '0':
                continue
            
            dfs(i, j, grid, grid_len, row_len)
            count += 1
    return count

def dfs(i, j, grid, grid_len, row_len):
    if i < 0 or j < 0 or i >= grid_len or j >= row_len:
        return
    if grid[i][j] == '1':
        grid[i][j] = '0'

        dfs(i + 1, j, grid, grid_len, row_len)
        dfs(i, j + 1, grid, grid_len, row_len)
        dfs(i - 1, j, grid, grid_len, row_len)
        dfs(i, j - 1, grid, grid_len, row_len)


def test_example_1():
    grid = [
        ["1","1","1","1","0"],
        ["1","1","0","1","0"],
        ["1","1","0","0","0"],
        ["0","0","0","0","0"]
    ]
    assert num_of_islands(grid) == 1

def test_example_2():
    grid = [
        ["1","1","0","0","0"],
        ["1","1","0","0","0"],
        ["0","0","1","0","0"],
        ["0","0","0","1","1"]
    ]
    assert num_of_islands(grid) == 3
    
def test_example_3():
    grid = [
        ["1","1","1"],
        ["0","1","0"],
        ["1","1","1"]
    ]
    assert num_of_islands(grid) == 1