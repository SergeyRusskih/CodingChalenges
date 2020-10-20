'''
Given a non-empty array of integers, every element appears three times except for one, 
which appears exactly once. Find that single one.

Note:

Your algorithm should have a linear runtime complexity. Could you implement it without 
using extra memory?

Example 1:

Input: [2,2,3,2]
Output: 3
Example 2:

Input: [0,1,0,1,0,1,99]
Output: 99

https://leetcode.com/problems/single-number-ii/discuss/43294/Challenge-me-thx
https://leetcode.com/problems/single-number-ii/discuss/43295/Detailed-explanation-and-generalization-of-the-bitwise-operation-method-for-single-numbers
'''
def single_number(numbers):
    one, two = 0, 0
    for number in numbers:
        one = (one | number) & ~two
        two = (two | number) & ~one
    return one

def test_example1():
    assert single_number([2,2,3,2]) == 3

def test_example2():
    assert single_number([0,1,0,1,0,1,99]) == 99