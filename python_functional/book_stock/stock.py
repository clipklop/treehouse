import json
from operator import itemgetter, attrgetter
from copy import copy
from functools import reduce, partial


class Book:
    def __init__(self, **kwargs):
        for k, v in kwargs.items():
            setattr(self, k, v)

    def __str__(self):
        return self.title

    def __repr__(self):
        return str(self)


def get_books(filename, raw=False):
    try:
        data = json.load(open(filename))
    except FileNotFoundError:
        return []
    else:
        if raw:
            return data['books']
        return [Book(**book) for book in data['books']]


BOOKS = get_books('books.json')
RAW_BOOKS = get_books('books.json', raw=True)
sorted_books = sorted(RAW_BOOKS, key=itemgetter('publish_date'))

# print([x['title'] for x in sorted_books])


def sales_price(book):
    """Apply a 20% discount to the book's price"""
    book = copy(book)
    book.price = round(book.price - book.price * .2, 2)
    return book


sales_books = list(map(sales_price, BOOKS))
# print([x.price for x in sales_books])


def has_roland(book):
    return any(['Roland' in subject for subject in book.subjects])


def titlecase(book):
    book = copy(book)
    book.title = book.title.upper()
    return book


# print(list(map(titlecase, filter(has_roland, BOOKS))))


def is_good_deal(book):
    return book.price <= 5


cheap_books = sorted(
    filter(is_good_deal, map(sales_price, BOOKS)),
    key=attrgetter('price')
)
# [(x, x.price) for x in cheap_books])
# print(f'{cheap_books[0]} for {cheap_books[0].price}$')
book_names = [x for x in cheap_books]
book_prices = [x.price for x in cheap_books]
# print('', *book_names, sep='\n')

# blowing my mind!
print('\n'.join('{0} for {1}$'.format(x, y) for x, y in zip(
    book_names, book_prices)))


def add_book_price(b1, b2):
    return b1 + b2


total = reduce(add_book_price, [b.price for b in BOOKS])
# print(total)

factorial = reduce(lambda x, y: x * y, range(1, 6), 1)
# print(factorial)
# print([b.price for b in BOOKS])


total1 = reduce(lambda x, y: x + y, [b.price for b in BOOKS])
# print(total1)
long_books1 = filter(lambda book: book.number_of_pages >= 600, BOOKS)
long_books2 = filter(lambda book: book.price <= 6, BOOKS)
# print(list(long_books1))
# print(len(list(long_books2)))

# When all you have is hammer, everything looks like a nail..


### PARTIALS ###
def mark_down(book, discount):
    book = copy(book)
    book.price = round(book.price - book.price * discount, 2)
    return book


standart = partial(mark_down, discount=.2)
half = partial(mark_down, discount=.5)
half_price_books = list(map(half, long_books1))
#print(half_price_books)


def curried_f(x, y=None, z=None):
    def f(x, y, z):
        return x**3 + y**2 + z

    if y is not None and z is not None:
        return f(x, y, z)
    if y is not None:
        return lambda z: f(x, y, z)

    return lambda y, z = None: (
        f(x, y, z) if (y is not None and z is not None)
        else (lambda z: f(x, y, z))
    )


print(curried_f(2, 3, 4))
g = curried_f(2)
print(g)
h = g(3)
print(h)
i = h(4)
print(i)
