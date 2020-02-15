#


class Protected:
    __security_name = "Security"

    def __security_method(self):
        return self.__security_name


prot = Protected()
print(dir(prot))
print(prot._Protected__security_name)
print(prot._Protected__security_method())
