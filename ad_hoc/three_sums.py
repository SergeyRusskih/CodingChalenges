def three_sum(nums, target):
    nums.sort()
    result = nums[0] + nums[1] + nums[2]

    for i in range(len(nums)-2):
        j, k = i+1, len(nums)-1
        while j < k:
            sum = nums[i]+nums[j]+nums[k]
            if sum == target:
                return sum

            if abs(sum-target) < abs(result-target):
                result = sum

            if sum - target > 0:
                k -= 1
            else:
                j += 1

                    
    return result

def test_1():
    result = three_sum([-1,2,1,-4], 1)
    assert result == 2