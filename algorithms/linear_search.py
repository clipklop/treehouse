"""
    * Algorithms: Linear Search
"""

from verify import verify, ARRAY


def linear_search(lst, target):
    """Returns the index position of target, else returns None."""
    try:
        return [i for i, v in enumerate(lst) if v == target][0]
    except IndexError:
        return None


found = linear_search(ARRAY, 10)
verify(found)

not_found = linear_search(ARRAY, 100)
verify(not_found)
