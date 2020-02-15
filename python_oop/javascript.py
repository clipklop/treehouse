#


class JavaScript(dict):
    def __getattribute__(self, item):
        try:
            return self[item]
        except KeyError:
            return super().__getattribute__(item)

js = JavaScript({"name": "MISHCA"})
print(js.name)
js.lang = 'Python'
print(js.lang)
