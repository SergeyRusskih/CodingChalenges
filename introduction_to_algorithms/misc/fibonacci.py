def fibonacci(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return calculate_fibonacci(0, 1, n - 2)

def calculate_fibonacci(a, b, n):
    return a + b if n == 0 else calculate_fibonacci(b, a + b, n - 1)

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