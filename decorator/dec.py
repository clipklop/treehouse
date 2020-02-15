"""
    * Basic decorator examples
"""
from functools import wraps


def outer(func):
    number = 5

    def inner():
        return number + func
    return inner


# x = outer(3)
# y = x()
# print(y)


def apply(func, x, y):
    return func(x, y)


def summy(x, y):
    return x + y


# print(apply(summy, 3, 6))


def close(x=5):

    def inner():
        return x + 3
    return inner


x = close(4)
# print(x())


def logme(func):
    import logging
    logging.basicConfig(level=logging.DEBUG)

    @wraps(func)
    def inner(*args, **kwargs):
        logging.debug(f'Called {func.__name__} with {args} and {kwargs}')
        return func(*args, **kwargs)
    # you could either this or functools.wraps
    # inner.__doc__ = func.__doc__
    # inner.__name__ = func.__name__
    return inner


@logme
def print_2():
    print(2)


# print_2()


@logme
def sub(x, y, switch=False):
    """ So, would this print or not??? """
    print(sub.__name__, sub.__doc__)
    return x - y if not switch else y - x


print(sub(9, 3, switch=True))
