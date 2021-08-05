# https://leetcode.com/explore/featured/card/top-interview-questions-easy/92/array/727/
def remove_duplicates(nums):
    current = None
    length = len(nums)

    i = 0
    while i < length:
        next = nums[i]
        if current == None or next != current:
            i += 1
            current = next
        else:
            nums.pop(i) # remove by index
            length -= 1

    return i

def test_1():
    result = remove_duplicates([0,0,1,1,1,2,2,3,3,4])
    assert result == 5