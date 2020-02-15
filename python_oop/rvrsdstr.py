#


class ReversedStr(str):
    """__new__
    operates on a class, and not on an instance
    it's safe (coz immutable) to use __new__ of
    inherit class directly, rather than for super
    """
    def __new__(*args, **kwargs):
        self = str.__new__(*args, **kwargs)
        self = self[::-1]
        return self


rs = ReversedStr('Doc')
rs1 = ReversedStr('hello')

print(rs, rs1)
