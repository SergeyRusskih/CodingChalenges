def fibonacci(number):
    if number == 0: return 0
    if number == 1: return 1

    a, b, count = 0, 1, 2
    while count <= number:
        a, b = b, a + b
        count += 1
    return b

def test_0():
    assert fibonacci(0) == 0

def test_1():
    assert fibonacci(1) == 1

def test_2():
    assert fibonacci(2) == 1

def test_3():
    assert fibonacci(3) == 2

def test_4():
    assert fibonacci(4) == 3

def test_5():
    assert fibonacci(5) == 5

def test_6():
    assert fibonacci(6) == 8