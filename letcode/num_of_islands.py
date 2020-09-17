import queue

def num_of_islands(grid):
    visited = [[ False for x in enumerate(grid)    ]
                       for y in enumerate(grid[0]) ]
    count = 0
    q = queue.Queue()
    for i, row in enumerate(grid):
        for j, cell in enumerate(row):
            if visited[i][j] or cell == '0':
                continue
            
            q.put((i, j))
            
            while q.qsize() != 0:
                current_row, current_column = q.get()
                if current_row + 1 < len(grid) and not visited[current_row + 1][current_column]:
                    q.put((current_row + 1, current_column))
                if current_column + 1 < len(row) and not visited[current_row][current_column + 1]:
                    q.put((current_row, current_column + 1))

                visited[current_row][current_column] = True
            
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