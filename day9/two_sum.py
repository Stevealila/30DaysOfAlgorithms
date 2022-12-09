"""
Question: Leetcode 1
Link: https://leetcode.com/problems/two-sum/

This implementation relies on hash maps, also referred to as dictionaries in py and objects in js. 
1. Store the difference (of the target and current array element) and the element's index.
2. Keep looping until you find an element that fills the missing difference i.e 9-2 = 7. And store the second element's index
3. return an array of the (first and second) indices.
"""

def twoSum(arr, target):
    # hm => hash map, i => current index
    hm = {}
    i = 0
    for n in arr:
        diff = target - n
        if n in hm: 
            return [hm[n], i]
            
        hm[diff] = i
        i += 1



nums = [2, 7, 11, 15]
print(twoSum(nums, 9)) # [0, 1]

nums = [3, 2, 4]
print(twoSum(nums, 6)) # [1, 2]

nums = [3, 3]
print(twoSum(nums, 6)) # [0, 1]