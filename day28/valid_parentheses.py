"""
Question: Leetcode 20
Link: https://leetcode.com/problems/valid-parentheses/


This implementation relies on a hash map and a stack. That's
    map the closing to the opening tags.
    loop through the string and pop off a matching opening tag (element) in the stack. 
    Otherwise, append the element to the stack.

"""

def validParentheses(s):
    hm = {'}':'{', ')':'(', ']':'['}
    stack = []


    for c in s:
        if c in hm:
            if stack and stack[-1] == hm[c]:
                stack.pop()
        else: 
            stack.append(c)

    return True if not stack else False

s = "()"
print(validParentheses(s)) #True
s = "()[]{}"
print(validParentheses(s)) #True
s = "(]"
print(validParentheses(s)) #False