"""
Question: Leetcode 53
Link: https://leetcode.com/problems/maximum-subarray/

This implimentation applies the Linear Search Algorithm
(https://github.com/Stevealila/30DaysOfAlgorithms/blob/main/day1/linear_search.js)
"""

def maximumSubarray(arr):
    # So far, maximum we have seen is the first element.
    maxSub = arr[0]
    currentSum = arr[0]

    for i in range(1, len(arr)):
        """
        If the current element is larger than the (previous) sum, 
        then we are better off without that sum.
        So, we reset the sum (to zero) 
        and start looking for maximum subarray from the current element.
        """
        if arr[i] > currentSum: currentSum = 0
        # Otherwise, continue updating the sum while tracking the largest sum attained.
        currentSum += arr[i] 
        maxSub = max(currentSum, maxSub)

    return maxSub


nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
print(maximumSubarray(nums)) #6

nums = [1]
print(maximumSubarray(nums)) #1

nums = [5,4,-1,7,8]
print(maximumSubarray(nums)) #23