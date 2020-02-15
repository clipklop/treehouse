# 2.
def combiner(lst):
    x = []
    s = ''
    num = 0
    for i in lst:
        if isinstance(i, str):
            s += i
        elif isinstance(i, (int, float)):
            num += i
    return f'{s}{num}'

# print(combiner(["apple", 5.2, "dog", 8]))


# Add a new property to the Rectangle class named area. It should
# calculate and return the area of the Rectangle instance (width * length)
class Rectangle:
    def __init__(self, width, length):
        self.width = width
        self.length = length

    @property
    def area(self):
        return self.width * self.length

    @property
    def perimeter(self):
        return self.length * 2 + self.width * 2
