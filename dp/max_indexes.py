def max_indexes(nums1, nums2):
    dp = [ [ 0 for _ in range(len(nums2)+1) ] for _ in range(len(nums1)+1)]
    for i in range(1, len(nums1)+1):
        for j in range(1, len(nums2)+1):
            if nums1[i-1] == nums2[j-1]:
                dp[i][j] = dp[i-1][j-1]+1

    return max(max(row) for row in dp)


def test_1():
    result = max_indexes([1,2,3,2,1], [3,2,1,4,7])
    assert result == 3

def test_2():
    result = max_indexes([0,0,0,0,0], [0,0,0,0,0])
    assert result == 5