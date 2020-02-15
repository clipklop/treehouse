#


class NumString:
    def __init__(self, value):
        self.value = str(value)

    def __str__(self):
        return self.value

    def __int__(self):
        return int(self.value)

    def __float__(self):
        return float(self.value)

    def __add__(self, other):
        if '.' in self.value:
            return float(self) + other
        return int(self) + other

    def __radd__(self, other):
        return self + other

    def __iadd__(self, other):
        self.value = self + other
        return self.value


five = NumString(5)
print(five + 4)

sixdotsix = NumString(6.6)
print(sixdotsix + 6)

seven = NumString(7)
print(7 + seven)

eight = NumString(8) + 8
print(eight)
