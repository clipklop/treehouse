"""
    * A module for verifying an algorithms.
"""


ARRAY = list(range(1, 99))
#ARRAY[-1], ARRAY[-2] = ARRAY[-2], ARRAY[-1]


def verify(index=None):
    if index is not None:
        print(f'Target found at index: {index}')
    else:
        print(f'Target not found in the list')


if __name__ == "__main__":
    verify()
