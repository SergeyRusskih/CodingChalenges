def zero_matrix(matrix):
    new_matrix = matrix.copy()
    for index, row in enumerate(matrix):
        new_matrix[index] = row.copy()
    
    for i, row in enumerate(matrix):
        for j, cell in enumerate(row):
            if cell == 0:
                for x, _ in enumerate(matrix):
                    new_matrix[x][j] = 0
                for y, _ in enumerate(row):
                    new_matrix[i][y] = 0
    return new_matrix

def test_zero_matrix():
    matrix = [[1, 1, 1, 1, 0, 1],
              [0, 1, 0, 1, 1, 1],
              [1, 1, 1, 1, 1, 1]]
    result = [[0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0],
              [0, 1, 0, 1, 0, 1]]
    assert zero_matrix(matrix) == result