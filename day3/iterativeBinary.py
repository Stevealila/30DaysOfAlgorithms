"""
Keep slicing the sorted list into two portions, 
while searching in the portion that is likely to contain the target.

Return True if the target is found. Otherwise, return None.

Runs in 0(log n).

Relies on the Two Pointers Technique.
"""


def binarySearch (list, target):
    # create two pointers to track the start and end indices of the list.
    left = 0
    right = len(list) - 1
    """
    Keep reassigning the two pointers until 
    (1) you locate the target or 
    (2) the two pointers collide in the searchable portion.
    """
    while left <= right: 

        midpoint = (left + right) // 2

        if list[midpoint] == target: 
            return True
        elif list[midpoint] < target: 
            left = midpoint + 1
        else: 
            right = midpoint - 1

    return None




list = [19, 23, 29, 31, 37, 41, 47]

print(binarySearch(list, 29)) # True
print(binarySearch(list, 9)) # None