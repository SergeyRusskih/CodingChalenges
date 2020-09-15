def sum_of_three(arr, value):
    for _, i, in enumerate(arr):
        for _, j in enumerate(arr):
            if i == j: 
                continue
            for _, k in enumerate(arr):
                if j == k:
                    continue
                if i + j + k == value:
                    return True
    return False

def test_is_sum_of_three():
    arr = [ 1, 2, 3, 4, 5, 6, 7, 8, 9]
    val = 7
    assert sum_of_three(arr, val)