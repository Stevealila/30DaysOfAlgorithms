"""
Question: Leetcode 167
Link: https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/description/

This implementation relies on the Two Pointers Technique.
"""

def twoSumII(arr, target):
    # Initially reference the first and last indices with left and right pointers. 
    left, right = 0, len(arr)-1
    """
    Keep reassigning the pointers,
    while summing them and 
    comparing the sum with target
    until (1) target found or (2) the pointers collide without finding the target.
    """
    while left <= right:
        # sum the two pointers
        sum = arr[left] + arr[right] 
        # target found? Return the matching indices (+1 because it is a 1-based array)
        if sum == target: return [left+1, right+1]
        # Otherwise, reassign the pointers.
        if sum < target: 
            left += 1
        else: 
            right -= 1

    # No matching indices
    return []


numbers = [2, 7, 11, 15]
print(twoSumII(numbers, 9)) #[1, 2]

numbers = [2, 3, 4]
print(twoSumII(numbers, 6)) #[1, 3]

numbers = [-1, 0]
print(twoSumII(numbers, -1)) #[1, 2]
