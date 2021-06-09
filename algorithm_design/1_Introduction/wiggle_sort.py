def wiggle_sort(nums):
    if len(nums) < 2:
        return nums

    sorted_nums = sorted(nums) # [ 6, 5, 4, 1, 1 ]
    i, j = 0, len(nums)-1
    for k in range(0, len(nums), 2):
        nums[k] = sorted_nums[i]
        if k+1 < len(nums):
            nums[k+1] = sorted_nums[j]
        i += 1
        j -= 1

    return nums


def test_1():
    result = wiggle_sort([1,5,1,6,4])
    assert result == [1,6,1,5,4]

def test_2():
    result = wiggle_sort([1,3,2,2,3,1])
    assert result == [2,3,1,3,1,2]