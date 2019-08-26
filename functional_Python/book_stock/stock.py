import json
from operator import itemgetter, attrgetter
from copy import copy
from functools import reduce


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
print(total)

factorial = reduce(lambda x, y: x * y, range(1, 6), 1)
print(factorial)
print([b.price for b in BOOKS])