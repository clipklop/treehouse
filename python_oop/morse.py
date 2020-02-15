class Letter:
    def __init__(self, pattern=None):
        self.pattern = pattern

    def __iter__(self):
        yield from self.pattern

    def __str__(self):
        output = []
        for blip in self:
            if blip == '.':
                output.append('dot')
            else:
                output.append('dash')
        return '-'.join(output)

    @classmethod
    def from_string(cls, string):
        output = []
        for sign in string.split('-'):
            if sign == 'dash':
                output.append('_')
            else:
                output.append('.')
        return cls(output)


class S(Letter):
    def __init__(self):
        pattern = ['.', '.', '.']
        super().__init__(pattern)


s = Letter('sos')
x = Letter.from_string("dash-dash-dash")
print(x)
