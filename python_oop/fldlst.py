#


class FilledList(list):
    """docstring for FilledList"""
    def __init__(self, count, value, *args, **kwargs):
        super().__init__()
        self.arg = arg
        for _ in range(count):
            self.append(copy.copy(value))


fl = FilledList(6, 9)
print(fl, len(fl))
