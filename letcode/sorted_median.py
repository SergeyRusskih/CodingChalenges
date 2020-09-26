# O(log (m+n))
def sorted_median(nums1, nums2):
    if len(nums1) + len(nums2) == 0:
        return 0
    if len(nums1) == 0:
        return get_simple_median(nums2)
    if len(nums2) == 0:
        return get_simple_median(nums1)
    
    return get_median(nums1, nums2, len(nums1) / 2, len(nums2) / 2)

def get_median(nums1, nums2, i, j):
    median1 = nums1[i]
    median2 = nums2[j]

    return 0


def test_6():
    nums1 = [1 ,2, 5, 8]
    nums2 = [3, 4, 6]
    assert sorted_median(nums1, nums2) == 4

def get_simple_median(nums):
    length = len(nums)
    if length % 2 == 0:
        return (nums[(length / 2) - 1] + nums[length / 2]) / 2
    return nums[length / 2]
    

def test_1():
    nums1 = [1,3]
    nums2 = [2]
    assert sorted_median(nums1, nums2) == 2

def test_2():
    nums1 = [1,2]
    nums2 = [3,4]
    assert sorted_median(nums1, nums2) == 2.5

def test_3():
    nums1 = [0,0]
    nums2 = [0,0]
    assert sorted_median(nums1, nums2) == 0

def test_4():
    nums1 = []
    nums2 = [1]
    assert sorted_median(nums1, nums2) == 1

def test_5():
    nums1 = [2]
    nums2 = []
    assert sorted_median(nums1, nums2) == 2