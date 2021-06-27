# https://leetcode.com/problems/powx-n/discuss/19560/Shortest-Python-Guaranteed
def my_pow(x, n):
    if not n: return 1
    if n < 0:
        return 1 / my_pow(x, -n)
    if n % 2:
        return x * my_pow(x, n-1)

    return my_pow(x*x, n/2)
    
def test_1():
    result = my_pow(2.00000, 10)
    assert result == 1024.00000

def test_2():
    result = my_pow(2.1, 3)
    assert result == 9.26100

def test_4():
    result = my_pow(2, 3)
    assert result == 8.0

def test_3():
    result = my_pow(2.00000, -2)
    assert result == 0.25000
