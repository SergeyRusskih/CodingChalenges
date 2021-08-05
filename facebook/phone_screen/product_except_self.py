# https://leetcode.com/problems/product-of-array-except-self/
def solution(nums):
    if not nums:
        return []
        
    if len(nums) < 2:
        return [0]

    previous = 1
    left_product = []
    for i in range(len(nums)):
        next = previous * nums[i]
        left_product.append(next)
        previous = next
            
    right_product = []
    previous = 1
    for i in range(len(nums)):
        next = previous * nums[~i]
        right_product.insert(0, next)
        previous = next
            
    answer = []
    for i in range(len(nums)):
        left = left_product[i-1] if i > 0 else 1
        right = right_product[i+1] if i+1 < len(right_product) else 1
            
        answer.append(left * right)
            
    return answer

def test_1():
    result = solution([1,2,3,4])
    assert result == [24,12,8,6]

def test_2():
    result = solution([-1,1,0,-3,3])
    assert result == [0,0,9,0,0]