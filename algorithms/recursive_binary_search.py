"""
    * Algorithms: Recursive Binary Search
"""

from verify import verify, ARRAY


def recursive_binary_search(lst, target, start=0, end=None):
    """Returns the index position of target if an array is sorted, else returns None."""
    if not lst == sorted(lst):
        print("Sorry, the algorithm wouldn't work until you sort the algorith. Let me do it for you...")
        lst = sorted(lst)

    if end is None:
        end = len(lst) - 1
    if start > end:
        return None

    midpoint = (start + end) // 2

    if lst[midpoint] == target:
        return midpoint
    else:
        if lst[midpoint] > target:
            return recursive_binary_search(lst, target, start, midpoint-1)
        else:
            return recursive_binary_search(lst, target, midpoint+1, end)


found = recursive_binary_search(ARRAY, 10)
verify(found)

not_found = recursive_binary_search(ARRAY, 100)
verify(not_found)
