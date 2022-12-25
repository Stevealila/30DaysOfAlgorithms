"""
Question: Leetcode 190
Link: https://leetcode.com/problems/reverse-bits/

This implementation relies on creating a 32-digit string, 
reversing it and 
returning the integer representation of the output.
"""

def reverseBits(n):
    s = list("{:032b}".format(n))
    s.reverse()
    return int("".join(s), 2)    


n = 0b00000010100101000001111010011100
print(reverseBits(n)) #964176192

n = 0b11111111111111111111111111111101
print(reverseBits(n)) #3221225471

