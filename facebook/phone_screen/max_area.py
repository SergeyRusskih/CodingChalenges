# https://leetcode.com/problems/container-with-most-water/
def solution(height):
    max_so_far, left, right = 0, 0, len(height)-1 
    while left < right:
        max_so_far = max(max_so_far, (right - left) * min(height[left], height[right]))
            
        if height[left] > height[right]:
            right -= 1
        else:
            left += 1
            
    return max_so_far
