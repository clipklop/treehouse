#


class Circle:
    def __init__(self, diameter):
        self.diameter = diameter

    @property
    def radius(self):
        return self.diameter / 2

small = Circle(10)
print(small.diameter)
print(small.radius)
