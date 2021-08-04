# !!! https://leetcode.com/problems/3sum/solution/
# two pinters solution
def three_sum(nums):
    if len(nums) < 3:
        return []

    nums.sort() 
    dups, res = set(), []

    for i in range(len(nums)):
        if i > 0 and nums[i-1] == nums[i]:
            continue

        n, m = i+1, len(nums)-1
        while n < m:
            three_sum = nums[i] + nums[n] + nums[m]
            if three_sum == 0:
                candidate = sorted([nums[i], nums[n], nums[m]])
                if tuple(candidate) not in dups:
                    dups.add(tuple(candidate))
                    res.append(candidate)
                n += 1
                m -= 1
                while n < m and nums[n] == nums[n-1]:
                    n += 1
            elif three_sum < 0:
                n += 1
            else:
                m -= 1

    return res

def test_1():
    result = three_sum([-1,0,1,2,-1,-4])
    assert result == [[-1,-1,2],[-1,0,1]]

def test_2():
    result = three_sum([])
    assert result == []

def test_3():
    result = three_sum([0])
    assert result == []