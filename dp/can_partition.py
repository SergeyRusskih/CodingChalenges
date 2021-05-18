# https://leetcode.com/problems/partition-equal-subset-sum/submissions/
def can_partition(nums):
    if len(nums) <= 1 or sum(nums) % 2 != 0:
        return False
        
    def dfs(i, target, cache):
        if target == 0: return True
        if target < 0: return False
        if target in cache: return False
            
        cache.add(target)
        for j in range(i+1, len(nums)):
            if dfs(j, target-nums[j], cache):
                return True
                
        return False
            
    return dfs(0, sum(nums) // 2, set())

def test_1():
    assert can_partition([1,5,11,5])

def test_2():
    assert not can_partition([1,2,5])