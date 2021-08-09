# https://leetcode.com/problems/combination-sum-iv/
def solution(nums, target):

    def find(current, memo):
        if current < 0: return 0
        if current == 0: return 1

        if current in memo:
            return memo[current]

        result = 0
        for num in nums:
            result += find(current - num, memo)
        
        memo[current] = result
        return result

    return find(target, {})

def test_1():
    assert solution([1,2,3], 4) == 7

def test_2():
    assert solution([9], 3) == 0