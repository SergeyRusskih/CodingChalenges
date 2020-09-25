import queue

def oranges_rotting(grid):

    rotten = queue.Queue()
    hours_count = 0
    while True:
        for i, row in enumerate(grid):
            for j, cell in enumerate(row):
                if cell == 2:
                    rotten.put((i, j))

        one_rotten = False
        while rotten.qsize() > 0:
            i, j = rotten.get()

            if rote_newighbours(i, j, grid):
                one_rotten = True

        if one_rotten:
            hours_count += 1
        else:
            break

    for i, row in enumerate(grid):
        for j, cell in enumerate(row):
            if cell == 1:
                return -1

    return hours_count

def rote_newighbours(i, j, grid):

    left = rote_neighbour(i - 1, j, grid)
    right = rote_neighbour(i + 1, j, grid)
    top = rote_neighbour(i, j + 1, grid)
    bottom = rote_neighbour(i, j - 1, grid)
    
    return left or right or top or bottom

def rote_neighbour(i, j, grid):
    if i < 0 or j < 0 or i >= len(grid) or j >= len(grid[0]):
        return False

    if grid[i][j] != 1:
        return False

    grid[i][j] = 2
    return True

def test_1():
    grid = [
        [2,1,1],
        [1,1,0],
        [0,1,1]
    ]
    assert oranges_rotting(grid) == 4

def test_2():
    grid = [
        [2,1,1],
        [0,1,1],
        [1,0,1]
    ]
    assert oranges_rotting(grid) == -1

def test_3():
    grid = [
        [0,2]
    ]
    assert oranges_rotting(grid) == 0