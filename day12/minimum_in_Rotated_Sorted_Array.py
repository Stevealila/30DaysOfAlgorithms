"""
Question: Leetcode 153
Link: https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/

This implimentation applies iterative binary search
(https://github.com/Stevealila/30DaysOfAlgorithms/blob/main/day3/iterativeBinary.py).
"""

def findMin(arr):
    left, right = 0, len(arr)-1

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] < arr[right]: 
            right = mid
        elif arr[mid] > arr[right]: 
            left = mid + 1
        else:
            return arr[mid]

    return arr[left]


nums = [3, 4, 5, 1, 2]
print(findMin(nums)) # 1

nums = [4, 5, 6, 7, 0, 1, 2]
print(findMin(nums)) # 0

nums = [11, 13, 15, 17]
print(findMin(nums)) # 11
