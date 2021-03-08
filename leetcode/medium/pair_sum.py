def array_pair_sum(nums):
    values = sorted(nums, reverse=True)
    result = 0
    for i in range(0, len(values), 2):
        if len(values) + 1 > i:
            result += min(values[i], values[i+1])

    return result


def test_example_1():
    result = array_pair_sum([1,4,3,2])
    assert result == 4

def test_example_2():
    result = array_pair_sum([6,2,6,5,1,2])
    assert result == 9    