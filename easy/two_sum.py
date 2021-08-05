'''
Given an array of integers nums and an integer target, 
return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, 
and you may not use the same element twice.

You can return the answer in any order.


Example 1:
Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Output: Because nums[0] + nums[1] == 9, we return [0, 1].

Example 2:
Input: nums = [3,2,4], target = 6
Output: [1,2]

Example 3:
Input: nums = [3,3], target = 6
Output: [0,1]
 

Constraints:

2 <= nums.length <= 105
-109 <= nums[i] <= 109
-109 <= target <= 109
Only one valid answer exists.
'''
def two_sum(numbers, target):
    for i, value1 in enumerate(numbers):
        for j in range(i + 1, len(numbers)):
            if value1 + numbers[j] == target:
                return [i, j]

    return ValueError

def test_example1():
    assert two_sum([2,7,11,15], 9) == [0,1]

def test_example2():
    assert two_sum([3,2,4], 6) == [1,2]

def test_example3():
    assert two_sum([3,3], 6) == [0,1]