"""
Question: Leetcode 152
Link: https://leetcode.com/problems/maximum-product-subarray/
"""


def maxProductSubarray(arr):
    # The maximum product we seen so far
    maxP = arr[0]
    """
    set maximum and minimum constituents to the neutral 1. 
    That's, any number multiplied by 1 will result to the number.
    """
    maxN, minN  = 1, 1

    for n in arr:
        # temporary (maxN) container to avoid overriding it in the minN equation.
        tmpMax = maxN * n

        maxN = max(n, minN * n, maxN * n)
        minN = min(n, minN * n, tmpMax)
        maxP = max(maxP, maxN)

    return maxP

nums = [2, 3, -2, 4]
print(maxProductSubarray(nums)) # 6

nums = [-2, 0, -1]
print(maxProductSubarray(nums)) # 0
