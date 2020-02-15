class Letter:
    def __init__(self, pattern=None):
        self.pattern = pattern

    def __str__(self):
        morse = []
        for p in self.pattern:
            morse.append('dot') if p == '.' else morse.append('dash')
        return '-'.join(morse)


class S(Letter):
    def __init__(self):
        pattern = ['.', '.', '.']
        super().__init__(pattern)


s = S()
print(str(s))
l = Letter(['.', '.', '.'])
print(str(l))

