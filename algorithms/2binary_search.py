"""
    * Algorithms: Binary Search
    * ordinary with a while loop 
    * and using a recursion
"""

from helper.verify import ARRAY, verify


def binary_search(lst, trgt):
    first = 0
    last = len(lst) - 1

    while first <= last:
        midpoint = (first + last) // 2

        if lst[midpoint] == trgt:
            return midpoint
        elif lst[midpoint] < trgt:
            first = midpoint + 1
        else:
            last = midpoint - 1


print(ARRAY)
print('Loop Binary Search:')
found = binary_search(ARRAY, 10)
verify(found)

not_found = binary_search(ARRAY, 100)
verify(not_found)
print("***\n")


def recursive_binary_search(lst, target, start=0, end=None):
    if end is None:
        end = len(lst) - 1
    if start > end:
        return -1, f"Target {target} not found."
    
    mid = (start + end) // 2

    if lst[mid] == target:
        return True, f"I've found target {lst[mid]} a {mid} index."
    else:
        if lst[mid] < target:
            return recursive_binary_search(lst, target, mid+1, end)
        else:
            return recursive_binary_search(lst, target, start, mid-1)


print('Recursive Binary Search:')
found = recursive_binary_search(ARRAY, 10)
verify(found)

not_found = recursive_binary_search(ARRAY, 100)
verify(not_found)
print("***\n")
