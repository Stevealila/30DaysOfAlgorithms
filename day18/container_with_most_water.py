"""
Question: Leetcode 11
Link: https://leetcode.com/problems/container-with-most-water/

This implimentation relies on the Two Pointers Technique.
"""

def containerWithMostWater(height):
    left, right = 0, len(height)-1
    maxArea = 0

    while left < right:
        # Area = Length * Width (height that won't spill our water.)
        area = (right - left) * min(height[left], height[right])
        maxArea = max(area, maxArea)
        # shift the smaller pointer (to continue maximizing the area)
        if height[left] < height[right]:
            left += 1
        else:
            right -= 1
    
    return maxArea



height = [1,8,6,2,5,4,8,3,7]
print(containerWithMostWater(height)) #49

height = [1,1]
print(containerWithMostWater(height)) #1