"""
This sorting algorithm relies on luck. That's
Check if a list is sorted. Otherwise, repeatedly reshuffle the elements.

The algorithm is suitable for learning purposes only. Otherwise, avoid it like hell.
"""

from random import shuffle

def bogoSort(arr):
    while notSorted(arr): shuffle(arr)
    return arr

def notSorted(arr):
    for i in range(1, len(arr)):
        if arr[i] < arr[i-1]:
            return True

arr = [2, 7, 3]
print(bogoSort(arr)) #[2, 3, 7]

