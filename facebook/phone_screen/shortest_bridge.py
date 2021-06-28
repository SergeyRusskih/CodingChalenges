# https://leetcode.com/problems/shortest-bridge/
def shortest_bridge(grid):

    def get_neighbours(i, j):
        neighbours = []
        if i-1 >= 0:
            neighbours.append((i-1, j))
        if i+1 < len(grid):
            neighbours.append((i+1, j))
        if j-1 >= 0:
            neighbours.append((i, j-1))
        if j+1 < len(grid[i]):
            neighbours.append((i, j+1))

        return neighbours

    queue = []
    def dfs(i, j):
        if grid[i][j] != 1:
            return

        grid[i][j] = -1
        queue.append((i, j))
        for x, y in get_neighbours(i, j):
            if 0 <= x < len(grid) and 0 <= y < len(grid[x]):
                dfs(x, y) 

    def find_first(value):
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == value:
                    return (i, j)

        return ValueError

    i, j = find_first(1)
    dfs(i, j)

    count = 0
    next = queue.copy()
    while next:
        next = []
        while queue:
            i, j = queue.pop(0)
            for x, y in get_neighbours(i, j):
                if 0 <= x < len(grid) and 0 <= y < len(grid[x]):
                    if grid[x][y] == 0:
                        grid[x][y] = -1
                        next.append((x, y))
                    elif grid[x][y] == 1:
                        return count

        count += 1
        queue = next

    return 0


def test_1():
    result = shortest_bridge(
        [
            [0,1],
            [1,0]
        ]
    )
    assert result == 1

def test_2():
    result = shortest_bridge(
        [
            [0,1,0],
            [0,0,0],
            [0,0,1]
        ]
    )
    assert result == 2

def test_3():
    result = shortest_bridge(
        [
            [1,1,1,1,1],
            [1,0,0,0,1],
            [1,0,1,0,1],
            [1,0,0,0,1],
            [1,1,1,1,1]
        ]
    )
    assert result == 1