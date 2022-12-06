"""
Question: Leetcode 33
Link: https://leetcode.com/problems/search-in-rotated-sorted-array/
"""

def searchRotatedSortedArray(nums, target):

    left, right = 0, len(nums) - 1

    while left <= right:

        mid = (left + right) // 2

        # target found 
        if nums[mid] == target: return mid


        # we are in left sorted sub array if the midpoint's element is greater than the leftmost element.
        if nums[mid] > nums[left]:
            if target < nums[mid] and target >= nums[left]:
                right = mid - 1
            else:
                left = mid + 1


        else:
            """
            if we are NOT in the left sorted portion, then we are in the right. 
            Because at any moment, at least one portion MUST be sorted.
            So, the opposites of the above conditions imply.
            """
            if target > nums[mid] and target <= nums[right]:
                right = mid - 1
            else:
                left = mid + 1

    return -1



nums = [4,5,6,7,0,1,2]
print(searchRotatedSortedArray(nums, 0)) # 4
print(searchRotatedSortedArray(nums, 3)) # -1
nums = [1]
print(searchRotatedSortedArray(nums, 0)) # -1
