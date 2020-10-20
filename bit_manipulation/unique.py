def find_unique(numbers):
    unique = 0
    for number in numbers:
        unique ^= number
    return unique

def test_find_unique():
    assert find_unique([2,2,1,3,3]) == 1