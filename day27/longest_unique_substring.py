"""
Question: Leetcode 3
Link: https://leetcode.com/problems/longest-substring-without-repeating-characters/

This implementation applies a hash map (python dictionary).
"""
def longestUniqueSub(s):
    start = 0
    length = 0
    hashMap = {}
    
    for i, n in enumerate(s):
        if n in hashMap and start <= hashMap[n]:
            start = hashMap[n] + 1
        else:
            length = max(length, i-start+1)
        hashMap[n] = i
    
    return length
        

s = "abcabcbb" 
print(longestUniqueSub(s)) #3

s = "bbbbb" # 1
print(longestUniqueSub(s)) #1

s = "pwwkew" # 3
print(longestUniqueSub(s)) #3