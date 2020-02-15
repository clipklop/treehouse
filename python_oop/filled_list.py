#


import copy


class FilledList(list):
    def __init__(self, count, value, *args, **kwargs):
        super().__init__()
        for _ in range(count):
            self.append(copy.copy(value))

fl = FilledList(5, [8, 9, 7])
fl[0][2] = 99
print(fl, len(fl))
