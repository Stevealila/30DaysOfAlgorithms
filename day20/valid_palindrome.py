"""
Question: Leetcode 125
Link: https://leetcode.com/problems/valid-palindrome/

This implementation relies on the Two Pointers technique.
"""

def validPalindrome(s):
    # Clean the data
    str = s.replace(" ", "")
    str = str.replace(",", "")
    str = str.replace(":", "")
    str = str.replace(".", "")
    str = str.replace(";", "")
    str = str.lower()

    # Initialize the two pointers
    left, right = 0, len(str)-1
    # Reassign the pointers until they collide or the subtrings don't match.
    while left <= right:
        if str[left] != str[right]: 
            return False
        left += 1
        right -= 1

    return True
    


s = "Alila"
print(validPalindrome(s)) # True

s = "A man, a plan, a canal: Panama"
print(validPalindrome(s)) # True

s = "race a car"
print(validPalindrome(s)) # False

s = " "
print(validPalindrome(s)) # True
