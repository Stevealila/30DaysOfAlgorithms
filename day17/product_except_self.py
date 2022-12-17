"""
Question: Leetcode 238
Link: https://leetcode.com/problems/product-of-array-except-self/

This implimentation relies on sets.
    Group the elements before and after the current one into prefix and postfix, respectively.
    Calculate the product of prefix and postfix.
"""


def productExceptSelf(arr):

    res = []

    for i in range(len(arr)):
        product, prefix, postfix = 1, set(), set()
        # prefix
        for pre in arr[:i]:
            prefix.add(pre)
        # postfix
        for post in arr[i+1:]:
            postfix.add(post)
        # product => prefix * postfix
        for n in prefix.union(postfix):
            product *= n
        res.append(product)

    return res

        
nums = [1, 2, 3, 4]
print(productExceptSelf(nums)) #[24, 12, 8, 6]

nums = [-1, 1, 0, -3, 3]
print(productExceptSelf(nums)) #[0, 0, 9, 0, 0]

