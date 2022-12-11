"""
Question: Leetcode 15
Link: https://leetcode.com/problems/3sum/

This implementation applies the concept of sum II 
(https://github.com/Stevealila/30DaysOfAlgorithms/blob/main/day10/two_sum_II.py). 

That's,

A) Sort the array,
B) Pivot an element before finding left and right pointers (in the subarray after the pivot) 
    whose sum with the pivot equates to zero. That's, pivot + left + right == 0.

    The first loop tracks the pivot, while the second tracks the two-sum (and three-sum).
    
"""

def threeSum(arr):
    arr.sort()
    final = []

    for i, n in enumerate(arr):
        # ignore duplicates
        if n == arr[i-1]: continue

        # two pointers to track left and right of the subarray that starts after n
        left, right = 1, len(arr)-1

        while left < right:
            sum = n + arr[left] + arr[right]

            if sum == 0: 
                final.append(n)
                final.append(arr[left])
                final.append(arr[right])
                return final

            elif sum < 0:
                left += 1
            else: 
                right -= 1

    return []






nums = [-7, 4, 2, 1, 3, -3]
print(threeSum(nums)) #[-7, 3, 4]

nums = [-1, 0, 1, 2, -1, -4]
print(threeSum(nums)) #[-1, -1, 2]

nums = [0, 1, 1]
print(threeSum(nums)) #[]