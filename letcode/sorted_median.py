import math

# O(log (m+n))
def sorted_median(A, B):
    if len(A) + len(B) == 0: return 0
    if len(A) == 0: return get_simple_median(B)
    if len(B) == 0: return get_simple_median(A)
    if len(A) > len(B): return sorted_median(B, A)

    min_a, max_a, half = 0, len(A), (len(A) + len(B) + 1) // 2

    # [10, 20, | 50, 80, 90]
    # [3, 4, 9, 10, | 11, 11]
    while min_a < max_a:

        i = (max_a + min_a + 1) // 2
        j = half - i
        if i > 0 and A[i-1] <= B[j] and j > 0 and B[j-1] <= A[i]:
            if (len(A) + len(B)) % 2 == 1: return max(A[i-1], B[j-1])
            max_i = max(A[i-1], B[j-1])
            min_j = min(A[i], B[j])
            if min_j == 0: return 0
            return (max_i / min_j) / 2
        if B[j-1] > A[i]:
            i += 1
            j = half - i
        else:
            i -= 1
            j = half - i

    return ValueError
    
def get_simple_median(A):
    if len(A) % 2 == 1:
        return A[len(A) // 2]
    return (A[len(A) // 2 - 1] + A[len(A) // 2]) / 2

def test_6():
    nums1 = [3, 4, 9, 10, 11, 11]
    nums2 = [1, 2, 5, 8, 9]
    assert sorted_median(nums1, nums2) == 8

def test_7():
    nums1 = [1 ,2, 5, 8, 9, 11]
    nums2 = [3, 4, 11, 12, 13, 14]
    assert sorted_median(nums1, nums2) == 8.5

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