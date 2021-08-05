def perfect_square(n):
    squares = []
    for i in range(1, n+1):
        square = i ** 2
        if square > n:
            break

        squares.append(square)

    to_check = {n}
    count = 0
    
    while to_check:
        count += 1
        tmp = set()

        for x in to_check:
            for y in squares:
                if x == y:
                    return count
                elif x < y:
                    break
                else:
                    tmp.add(x - y)

        to_check = tmp

    return count



def test_example_1():
    result = perfect_square(1)
    assert result == 1

def test_example_4():
    result = perfect_square(4)
    assert result == 1

def test_example_12():
    result = perfect_square(12)
    assert result == 3

def test_example_13():
    result = perfect_square(13)
    assert result == 2

def test_example_18():
    result = perfect_square(18)
    assert result == 2