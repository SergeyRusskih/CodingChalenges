# https://leetcode.com/problems/maximum-subarray/
def solution(nums):
    max_global = max_so_far = float('-inf')
    for num in nums:
        max_so_far = max(num, num + max_so_far)
        max_global = max(max_global, max_so_far)

    return max_global

def test_1():
    result = solution([-2,1,-3,4,-1,2,1,-5,4])
    assert result == 6

def test_2():
    result = solution([5,4,-1,7,8])
    assert result == 23

def test_3():
    result = solution([1])
    assert result == 1

