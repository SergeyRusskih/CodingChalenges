def two_sum_less_k(nums, k):
    result = -1
    nums.sort()

    i, j = 0, len(nums)-1
    while i < j:
        candidate = nums[i] + nums[j]
        if candidate >= k:
            j -= 1
        else:
            result = max(result, candidate)
            i += 1

    return result

def test_1():
    result = two_sum_less_k([34,23,1,24,75,33,54,8], 60)
    assert result == 58

def test_2():
    result = two_sum_less_k([10,20,30], 15)
    assert result == -1