# https://leetcode.com/problems/search-in-rotated-sorted-array/
def solution(nums, target):

    def is_in_left(start, middle, end):
        if nums[start] > nums[middle] and (nums[start] < target or nums[middle] > target):
            return True
        
        if nums[start] < nums[middle] and nums[start] < target and nums[middle] > target:
            return True

        return False

    def find(start, middle, end):
        if nums[start] == target: return start
        if nums[middle] == target: return middle
        if nums[end] == target: return end
        if start == middle or end == middle: return -1

        in_left = is_in_left(start, middle, end)

        start = start if in_left else middle
        end = end if not in_left else middle
        middle = start + (end - start) // 2

        return find(start, middle, end)

    return find(0, (len(nums)-1) // 2, len(nums)-1)

def test_6():
    assert solution([4,5,6,7,8,1,2,3], 8) == 4

def test_1():
    assert solution([5,1,2,3,4], 1) == 1

def test_2():
    assert solution([3,4,5,1,2], 1) == 3

def test_3():
    assert solution([1,2,3,4,5], 2) == 1

def test_4():
    assert solution([1,2], 1) == 0

def test_5():
    assert solution([2,1], 1) == 1