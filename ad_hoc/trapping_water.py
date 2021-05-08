def trapping_wather(height):
    volume, left_max, right_max = 0, 0, 0
    left, right = 0, len(height)-1
    while left <= right:
        left_max = max(left_max, height[left])
        right_max = max(right_max, height[right])
        if left_max < right_max:
            volume += left_max - height[left]
            left += 1
        else:
            volume += right_max - height[right]
            right -= 1


    return volume

def test_1():
    result = trapping_wather([0,1,0,2,1,0,1,3,2,1,2,1])
    assert result == 6

def test_2():
    result = trapping_wather([4,2,0,3,2,5])
    assert result == 9