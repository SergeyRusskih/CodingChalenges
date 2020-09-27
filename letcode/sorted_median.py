# O(log (m+n))
def sorted_median(A, B):
    if len(A) + len(B) == 0: return 0
    if len(A) == 0: return get_simple_median(B)
    if len(B) == 0: return get_simple_median(A)
    if len(A) > len(B): return sorted_median(B, A)

    total_length = len(A) + len(B)
    min_a, max_a, half, is_odd = 0, len(A), (total_length + 1) // 2, (total_length) % 2 == 1

    while min_a <= max_a:
        i = (max_a + min_a) // 2
        j = half - i

        left_a = A[i-1] if i > 0 else float('-inf')
        right_a = A[i] if len(A) > i else float('inf')

        left_b = B[j-1] if j > 0 else float('-inf')
        right_b = B[j] if len(B) > j else float('inf')

        if i < len(A) and left_b > right_a: min_a = i + 1
        elif i > 0 and left_a > right_b: max_a = i - 1
        else:
            max_left = max(left_a, left_b)
            if is_odd: return max_left
            min_right = min(right_a, right_b)
            return (max_left + min_right) / 2

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

def test_8():
    nums1 = [3]
    nums2 = [-2,-1]
    assert sorted_median(nums1, nums2) == -1

def test_9():
    nums1 = [3]
    nums2 = [1,2]
    assert sorted_median(nums1, nums2) == 2

def test_10():
    nums1 = [4]
    nums2 = [1,2,3]
    assert sorted_median(nums1, nums2) == 2.5