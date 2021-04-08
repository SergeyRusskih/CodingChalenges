def dail_pad(n):

    MOD = 10 ** 9 + 7
    pad = [ [ 4, 6 ], [ 6, 8 ], [ 7, 9 ], [ 4, 8 ], [ 3, 9, 0 ], [], [ 1, 7, 0 ], [ 2, 6 ], [ 1, 3 ], [ 2, 4 ] ]
    current = [1] * 10

    current_n = 1
    while n > current_n:
        next = [0] * 10
        for index, count in enumerate(current):
            for neighbour in pad[index]:
                next[neighbour] += count
                next[neighbour] %= MOD

        current = next
        current_n += 1

    return sum(current) % MOD

    
def test_dail_pad_1():
    result = dail_pad(1)
    assert result == 10

def test_dail_pad_2():
    result = dail_pad(2)
    assert result == 20

def test_dail_pad_3():
    result = dail_pad(3)
    assert result == 46

def test_dail_pad_4():
    result = dail_pad(4)
    assert result == 104

def test_dail_pad_3131():
    result = dail_pad(3131)
    assert result == 136006598