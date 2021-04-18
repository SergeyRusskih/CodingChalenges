def rob(num):
    if not num:
        return 0

    if len(num) == 1:
        return num[0]

    if len(num) == 2:
        return max(num[0], num[1])

    sums = [0] * len(num)
    sums[0] = num[0]
    sums[1] = max(num[0], num[1])

    for i in range(2, len(num)):
        sums[i] = max(sums[i-1], sums[i-2]+num[i])

    return sums[-1]


def test_rob_1():
    result = rob([1,2,3,1])
    assert result == 4

def test_rob_2():
    result = rob([2,7,9,3,1])
    assert result == 12

def test_rob_3():
    result = rob([8,1,1,9])
    assert result == 17