# https://leetcode.com/problems/count-number-of-nice-subarrays/
def number_of_subarrays(nums, k):

    def at_most(k):
        res = i = 0
        for j in range(len(nums)):
            k -= nums[j] % 2
            while k < 0:
                k += nums[i] % 2
                i += 1
            res += j - i + 1

        return res

    return at_most(k) - at_most(k-1)

def test_1():
    result = number_of_subarrays([1,1,2,1,1], 3)
    assert result == 2

def test_2():
    result = number_of_subarrays([2,4,6], 1)
    assert result == 0

def test_3():
    result = number_of_subarrays([2,2,2,1,2,2,1,2,2,2], 2)
    assert result == 16