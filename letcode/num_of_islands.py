import queue as queue

def num_of_islands(grid):
    count = 0
    q = queue.Queue()
    grid_len = len(grid)
    row_len = 0
    if grid_len > 0:
        row_len = len(grid[0])
    for i in range(grid_len):
        for j in range(row_len):
            if grid[i][j] == '0':
                continue
            
            q.put((i, j))
            
            while q.qsize() != 0:
                current_row, current_column = q.get()
                next_row = current_row + 1
                if next_row < grid_len:
                    if grid[next_row][current_column] != '0':
                        q.put((next_row, current_column))
                        grid[next_row][current_column] = '0'
                next_row = current_row - 1
                if next_row >= 0:
                    if grid[next_row][current_column] != '0':
                        q.put((next_row, current_column))
                        grid[next_row][current_column] = '0'
                next_column = current_column + 1
                if next_column < row_len:
                    if grid[current_row][next_column] != '0':
                        q.put((current_row, next_column))
                        grid[current_row][next_column] = '0'
                next_column = current_column - 1
                if next_column >= 0:
                    if grid[current_row][next_column] != '0':
                        q.put((current_row, next_column))
                        grid[current_row][next_column] = '0'
            count += 1
    return count

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