"""
    *** Exercises from course objectives
"""
import datetime


# task 2.-1
temperatures = [
    37,
    0,
    25,
    100,
    13.2,
    29.9,
    18.6,
    32.8
]


def c_to_f(temp):
    """Returns Celsius temperature as Fahrenheit"""
    return temp * (9/5) + 32


good_temps = [c_to_f(x) for x in temperatures if x >= 9 and x <= 32.6]
# print(good_temps)


# task 2.-2
birthdays = [
    datetime.datetime(2012, 4, 29),
    datetime.datetime(2006, 8, 9),
    datetime.datetime(1978, 5, 16),
    datetime.datetime(1981, 8, 15),
    datetime.datetime(2001, 7, 4),
    datetime.datetime(1999, 12, 30)
]

today = datetime.datetime.today()


def is_over_13(dt):
    return (today - dt).days >= 4745


def date_string(dt):
    return dt.strftime('%B %d')


birth_dates = list(map(date_string, filter(is_over_13, birthdays)))
# print(birth_dates)


PRICE = [
    13.55, 7.99, 7.99, 8.99, 7.99, 7.99, 12.69, 13.59, 8.99, 8.06,
    12.75, 7.57, 7.99, 6.6, 7.66, 4.83, 3.5, 4.99, 6.6, 7.6, 7.95,
    5.79, 10.08, 8.24, 8.99, 3.78, 7.61, 4.94
]


def long_total(a=None, b=None, books=None):
    if a is None and b is None and books is None:
        return None
    if a is None and b is None and books is not None:
        a = books.pop(0)
        b = books.pop(0)
        return long_total(a, b, books)
    if a is not None and b is None and books is not None and books:
        b = books.pop(0)
        return long_total(a, b, books)
    if a is not None and b is not None and books is not None:
        return long_total(a+b, None, books)
    if a is not None and b is not None and not books:
        return long_total(a+b, None, None)
    if a is not None and b is None and not books or books is None:
        return a


# print(long_total(None, None, PRICE))


courses = {'count': 2,
           'title': 'Django Basics',
           'prereqs': [{'count': 3,
                     'title': 'Object-Oriented Python',
                     'prereqs': [{'count': 1,
                               'title': 'Python Collections',
                               'prereqs': [{'count':0,
                                         'title': 'Python Basics',
                                         'prereqs': []}]},
                              {'count': 0,
                               'title': 'Python Basics',
                               'prereqs': []},
                              {'count': 0,
                               'title': 'Setting Up a Local Python Environment',
                               'prereqs': []}]},
                     {'count': 0,
                      'title': 'Flask Basics',
                      'prereqs': []}]}


def prereqs(data, pres=None):
    """
loop through each of the items in the `prereqs` property of the data
for each prepreq, add it's title to the set
then we want to add each of the prereq's prereqs to the set.
...This is where we'll use recursion.
you'll want to call this function within itself
... the data argument will be the prereqs and the pres argument
 will be the existing set.
    """
    pres = pres or set()
    for prereq in data['prereqs']:
        pres.add(prereq['title'])
        prereqs(prereq, pres)
    return pres


# print(prereqs(courses))
