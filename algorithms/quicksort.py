"""
    * Algorithms: Quicksort
"""

import random
import sys
import os

from helper.load import load_numbers


numbers = load_numbers(sys.argv[1])


def quicksort(values):
    """Divide and Conquer"""
    if len(values) <= 1:
        return values

    pivot = values[0]
    less = [x for x in values[1:] if x <= pivot]
    greater = [x for x in values[1:] if x >= pivot]
    
    # print("%15s %1s %-15s" % (less, pivot, greater))
    return quicksort(less) + [pivot] + quicksort(greater)


print(quicksort(numbers))
