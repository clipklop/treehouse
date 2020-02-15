#


class Circle:
    def __init__(self, diameter):
        self.diameter = diameter

    @property  # you can't set the new value to return @property
    def radius(self):
        return self.diameter / 2

    @radius.setter  # but it's possible using setter method
    def radius(self, radius):
        self.diameter = radius * 2


small = Circle(12)
print(small.diameter)
print(small.radius)  # note: there's no brackets for method invocation
small.radius = 10
print(small.diameter)
print(small.radius)
