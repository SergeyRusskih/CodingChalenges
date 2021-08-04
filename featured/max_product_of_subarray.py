# https://leetcode.com/problems/maximum-product-subarray/
# https://leetcode.com/problems/maximum-subarray/submissions/
# https://leetcode.com/problems/subarray-product-less-than-k/
#
# https://medium.com/@rsinghal757/kadanes-algorithm-dynamic-programming-how-and-why-does-it-work-3fd8849ed73d
#
##################################
#####                        #####
#####   Kadane's algorithm   #####
#####                        #####
##################################
#
# ~ x Returns the complement of x - the number you get by switching each 1 for a 0 and each 0 for a 1. 
# This is the same as -x - 1.
def max_product_of_subarray(nums):
    prefix, suffix, max_so_far = 0, 0, float('-inf')
    for i in range(len(nums)):
        prefix = (prefix or 1) * nums[i] # calculate prefix product
        siffix = (suffix or 1) * nums[~i] # calculate suffix product
        max_so_far = max(prefix, siffix, max_so_far) # return the max

    return max_so_far

def test_1():
    result = max_product_of_subarray([2,3,-2,4])
    assert result == 6

def test_2():
    result = max_product_of_subarray([-2,0,-1])
    assert result == 0