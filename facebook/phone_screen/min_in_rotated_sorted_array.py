# https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/submissions/
def solution(nums):
    if len(nums) == 1:
        return nums[0]

    def find(start, middle, end):
        if start == middle or middle == end:
            return min(nums[start], nums[middle], nums[end])

        is_in_left = nums[end] > nums[start] or nums[end] > nums[middle]
        start = start if is_in_left else middle
        end = end if not is_in_left else middle
        middle = start + (end - start) // 2
        
        return find(start, middle, end)

    return find(0, (len(nums)-1) // 2, len(nums)-1)


def test_1():
    assert solution([5,1,2,3,4]) == 1

def test_2():
    assert solution([3,4,5,1,2]) == 1

def test_3():
    assert solution([1,2,3,4,5]) == 1

def test_4():
    assert solution([1,2]) == 1

def test_5():
    assert solution([2,1]) == 1