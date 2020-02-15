"""
    * Algorithms: Selection Search
"""

import random
import sys
import os

from helper.load import load_numbers


numbers = load_numbers(sys.argv[1])


def my_selection_sort(values):
    """My implementation of Selection sort."""
    new_array = []
    while values:
        min_v = values[0]
        min_i = 0
        for i in range(len(values)):
            if values[i] < min_v:
                min_v = values[i]
                min_i = i
        new_array.append(values.pop(min_i))

    return new_array


def selection_sort(values):
    sorted_list = []
    # print("%-25s %-25s" % (values, sorted_list))
    for i in range(len(values)):
        i_to_move = min_index(values)
        sorted_list.append(values.pop(i_to_move))
        # print("%-25s %-25s" % (values, sorted_list))
    return sorted_list


def min_index(values):
    min_i = 0
    for i in range(1, len(values)):
        if values[i] < values[min_i]:
            min_i = i
    return min_i


print(selection_sort(numbers))
