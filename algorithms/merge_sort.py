"""
    * Algorithms: Merge Sort
"""

import random
import sys
import os

from helper.load import load_numbers


numbers = load_numbers(sys.argv[1])


def merge_sort(values):
    """My implementation of Merge sort."""
    if len(values) <= 1:
        return values

    middle_idx = len(values) // 2
    left_values = merge_sort(values[:middle_idx])
    right_values = merge_sort(values[middle_idx:])
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


print(numbers)
print(merge_sort(numbers))
