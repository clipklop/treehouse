"""
    * Merge sort implementation
"""

import sys

from helper.load import load_numbers


numbers = load_numbers(sys.argv[1])


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


def my_merge_sort(values):
    """My implementation of Merge sort."""
    if len(values) <= 1:
        return values

    middle_idx = len(values) // 2
    left_values = my_merge_sort(values[:middle_idx])
    right_values = my_merge_sort(values[middle_idx:])
    print("%15s %-15s" % (left_values, right_values))

    sorted_values = []
    left_idx, right_idx = 0, 0

    while left_idx < len(left_values) and right_idx < len(right_values):
        if left_values[left_idx] < right_values[right_idx]:
            sorted_values.append(left_values[left_idx])
            left_idx += 1
        else:
            sorted_values.append(right_values[right_idx])
            right_idx += 1    

    # if something is still remaining unsorted, just add it to sorted list
    sorted_values += left_values[left_idx:]
    sorted_values += right_values[right_idx:]

    return sorted_values


def verify_sorted(lst):
    n = len(lst)

    if n <= 1:
        return True

    return lst[0] <= lst[1] and verify_sorted(lst[1:])


test = [54,62,93,17,77,31,44,55,20]
print(merge_sort(test))
print(verify_sorted(test))
print(verify_sorted(merge_sort(test)))

print(numbers)
print(merge_sort(numbers))
print(my_merge_sort(numbers))

print(verify_sorted(numbers))
print(verify_sorted(my_merge_sort(numbers)))

