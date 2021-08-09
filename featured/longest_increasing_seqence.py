# https://leetcode.com/problems/longest-increasing-subsequence/
# https://en.wikipedia.org/wiki/Patience_sorting
#
#
##################################
#####                        #####
#####    Patience sorting    #####
#####                        #####
##################################
#
# 1. Initialize an array sub which contains the first element of nums.
# 2. Iterate through the input, starting from the second element. For each element num:
#    - If num is greater than any element in sub, then add num to sub.
#    - Otherwise, perform a binary search in sub to find the smallest element that is greater than or equal to num.
#      Replace that element with num.
# 3. Return the length of sub.
#
def solution(nums):
    if not nums:
        return 0

    sub = [nums[0]]
    for num in nums[1:]:
        if num > sub[-1]:
            sub.append(num)
        else:
            i, j = 0, len(sub)-1
            while i < j:
                middle = (i + j) // 2
                if sub[middle] < num:
                    i = middle + 1
                else:
                    j = middle

            sub[i] = num

    return len(sub)


def test_1():
    assert solution([10,9,2,5,3,7,101,18]) == 4

def test_2():
    assert solution([0,1,0,3,2,3]) == 4

def test_3():
    assert solution([7,7,7,7,7,7,7]) == 1