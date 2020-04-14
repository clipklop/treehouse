# *
# ** Merge sort implementation
# *

def merge_sort(lst):
    """
    Sorts a list in ascending order
    Returns a new sorted list

    Divide: Find the midpoint of the list and divide into sublists
    Conquer: Recursively sort the sublists created in previous step
    Combine: Merge the sorted sublists created in previous tep

    Takes O(n log n) time
    """
    if len(lst) <= 1:
        return lst

    mid = len(lst) // 2
    left, right = merge_sort(lst[:mid]), merge_sort(lst[mid:])

    l = []
    i, j = 0, 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            l.append(left[i])
            i += 1
        else:
            l.append(right[j])
            j += 1

    # in case if 'left' and 'right' parts are not equal
    l += left[i:]
    l += right[j:]

    return l


def verify_sorted(lst):
    n = len(lst)

    if n <= 1:
        return True

    return lst[0] <= lst[1] and verify_sorted(lst[1:])


test = [54,62,93,17,77,31,44,55,20]
print(merge_sort(test))
print(verify_sorted(merge_sort(test)))
print(verify_sorted(test))
