"""
    * Algorithms: Bogo Search sic!
"""

import random
import sys
import os

from helper.load import load_numbers

print(sys.argv)
numbers = load_numbers(sys.argv[1])


def is_sorted(values):
    for index in range(len(values) - 1):
        if values[index] > values[index + 1]:
            return False
    return True


def bogo_sort(values):
    attempts = 0
    while not is_sorted(values):
        random.shuffle(values)
        attempts += 1
    return f'It took you {attempts} attempts to sort this {values} list'


if __name__ == "__main__":
    print(bogo_sort(numbers))
