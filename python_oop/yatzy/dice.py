"""
    * Yatzy game
"""
import random


class Die:
    def __init__(self, sides=2, value=0):
        if not sides >= 2:
            raise ValueError('Must have at least 2 sides')
        if not isinstance(sides, int) or not isinstance(value, int):
            raise ValueError('Sides or Value must be a whole number')
        self.value = value or random.randint(1, sides)

    def __int__(self):
        return self.value

    def __eq__(self, other):
        return int(self) == other

    def __ne__(self, other):
        return int(self) != other

    def __lt__(self, other):
        return int(self) < other

    def __gt__(self, other):
        return int(self) > other

    def __le__(self, other):
        return int(self) <= other

    def __ge__(self, other):
        return int(self) >= other

    def __add__(self, other):
        return int(self) + other

    def __radd__(self, other):
        return self + other

    def __repr__(self):
        return str(self.value)


class D6(Die):
    def __init__(self, sides=6, value=0):
        super().__init__(sides=sides, value=value)


if __name__ == "__main__":
    d4 = Die(5)
    print(d4.value)

    d6 = D6()
    print(d6.value, int(d6), d6 > 4, d6 == 6, d6 != 7, d6 < 5, d6 >= 3, d6 + 9, 8 + d6)
