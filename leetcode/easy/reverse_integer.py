'''
Share
Given a 32-bit signed integer, reverse digits of an integer.

Note:
Assume we are dealing with an environment that could only store integers within 
the 32-bit signed integer range: [−2^31,  2^31 − 1]. For the purpose of this problem, 
assume that your function returns 0 when the reversed integer overflows.


Example 1:
Input: x = 123
Output: 321

Example 2:
Input: x = -123
Output: -321

Example 3:
Input: x = 120
Output: 21

Example 4:
Input: x = 0
Output: 0
'''

def reverse(value):

    string_value = str(value)
    char_list = []

    for c in reversed(string_value):
        if c == '-':
            char_list.insert(0, c)
        else:
            char_list.append(c)

    result = int("".join(char_list))
    if(abs(result) > (2 ** 31 - 1)):
        return 0
    return result

def test_example1():
    assert reverse(123) == 321

def test_example2():
    assert reverse(-123) == -321

def test_example3():
    assert reverse(0) == 0

def test_example4():
    assert reverse(1534236469) == 0