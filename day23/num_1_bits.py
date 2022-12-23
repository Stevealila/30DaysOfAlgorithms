"""
Question: Leetcode 191
Link: https://leetcode.com/problems/number-of-1-bits/
"""

def num1Bits(n):
    total = 0

    while n > 0:
        total += n % 2
        # shift the remaining bits to the right by 1
        n = n >> 1

    return total

n = 0b00000000000000000000000000001011
print(num1Bits(n)) #3
n = 0b00000000000000000000000010000000
print(num1Bits(n)) #1
n = 0b11111111111111111111111111111101
print(num1Bits(n)) #31