"""
    * Algorithms: Binary Search
"""

from helper.verify import verify, ARRAY


def binary_search(lst, target):
    """Returns the index position of target if an array is sorted, else returns None."""
    if not lst == sorted(lst):
        print("Sorry, the algorithm wouldn't work until you sort the algorith. Let me do it for you...")
        lst = sorted(lst)

    first = 0
    last = len(lst) - 1

    while first <= last: # subtle logic here - this check is also makes sure that array is not empty, coz 'first' would be always greater than 'last'
        midpoint = (first + last) // 2

        if lst[midpoint] == target:
            return midpoint
        elif lst[midpoint] < target:
            first = midpoint + 1
        else:
            last = midpoint - 1

    return None


found = binary_search(ARRAY, 10)
verify(found)

not_found = binary_search(ARRAY, 100)
verify(not_found)
