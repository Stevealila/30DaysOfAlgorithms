"""
Locate the minimum element and append it to second list,
while removing the element from its initial parent.
Repeat the process until the original list is empty.

Runs in 0(n^2)
"""

def selectionSort(arr):
    sorted_arr = []

    while len(arr) > 0:
        smallest = min(arr)
        sorted_arr.append(smallest)
        arr.remove(smallest)

    return sorted_arr


arr = [19, 13, 17, 15, 11]
print(selectionSort(arr)) #[11, 13, 15, 17, 19]
