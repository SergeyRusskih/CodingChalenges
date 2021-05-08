def min_move(machines):
    total = sum(machines)
    if total % len(machines) != 0:
        return -1

    avg = total // len(machines)
    count = 0
    for item in machines:
        if item < avg:
            count += avg-item

    return count

def test_4():
    res = min_move([4,0,0,4])
    assert res == 2

def test_1():
    res = min_move([1,0,5])
    assert res == 3

def test_2():
    res = min_move([0,3,0])
    assert res == 2

def test_3():
    res = min_move([0,2,0])
    assert res == -1