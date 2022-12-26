
"""
Question: Leetcode 5
Link: https://leetcode.com/problems/longest-palindromic-substring/

Locate a palindromic substring and spread out as far (left and right) as possible,
updating the substring if its length is greater than that of its predecessor.
"""
def longestPSub(s):
    string = ""
    strLength = 0

    for i in range(len(s)):
        # Odd palindrome
        left, right = i, i
        while left >= 0 and right < len(s) and s[left] == s[right]:
            length = right - left + 1
            if length > strLength:
                string = s[left:right+1]
                strLength = length
            left -= 1
            right += 1
        # Even palindrome
        left, right = i, i+1
        while left >= 0 and right < len(s) and s[left] == s[right]:
            length = right - left + 1
            if length > strLength:
                string = s[left:right+1]
                strLength = length
            left -= 1
            right += 1

    return string


s = "babad"
print(longestPSub(s)) #bab
s = "cbbd"
print(longestPSub(s)) #bb