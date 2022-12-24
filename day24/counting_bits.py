"""
Question: Leetcode 338
Link: https://leetcode.com/problems/counting-bits/

count 1 bits per iteration (https://github.com/Stevealila/30DaysOfAlgorithms/blob/main/day23/num_1_bits.py) then
append each count to an array.
"""

def countingBits (n):
    arr = []
    for i in range(n+1): arr.append(count1Bits(i))
    return arr

def count1Bits(n):
    n = int(bin(n), 2)
    count = 0

    while n > 0:
        count += n % 2
        n = n >> 1

    return count

n = 2
print(countingBits(n)) #[0,1,1]

n = 5
print(countingBits(n)) #[0,1,1,2,1,2]
