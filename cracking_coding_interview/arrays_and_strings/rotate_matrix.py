def rotate(matrix):
    new_matrix = [[ 0 for x in enumerate(matrix)]
                      for y in enumerate(matrix)]
    for i, row in enumerate(matrix):
        for j, _ in enumerate(row):
            new_matrix[i][j] = matrix[len(matrix) - (1 + j)][i]       
    return new_matrix

def test_simple_matrix():
    simple_matrix = [[0, 1, 2],
                     [3, 4, 5],
                     [6, 7, 8]]
    result = [[6, 3, 0],        
              [7, 4, 1],
              [8, 5, 2]]
    assert rotate(simple_matrix) == result