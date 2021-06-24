def max_sum_three(nums):

    def helper(arr, remainder, substracted):
        if remainder < 3: return 0
        if remainder % 3 == 0: return remainder

        result = 0
        for i, item in enumerate(arr):
            if i in substracted: continue
            substracted.add(i)
            result = max(result, helper(arr, remainder-item, substracted))
            substracted.remove(i)
        
        return result
        
    return helper(nums, sum(nums), set())

def test_4():
    result = max_sum_three([3,1])
    assert result == 3

def test_1():
    result = max_sum_three([3,6,5,1,8])
    assert result == 18

def test_2():
    result = max_sum_three([4])
    assert result == 0

def test_3():
    result = max_sum_three([1,2,3,4,4])
    assert result == 12