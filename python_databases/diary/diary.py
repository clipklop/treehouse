#!/usr/bin/env python3
"""
    * CLI Diary app
"""


from collections import OrderedDict
import peewee as pw
import datetime


DB = pw.SqliteDatabase('diary.db')


class Entry(pw.Model):
    content = pw.TextField()
    datetime = pw.DateTimeField(default=datetime.datetime.now)

    class Meta:
        database = DB


def initialize():
    """Create the database and the table if they don't exist."""
    DB.connect()
    DB.create_tables([Entry], safe=True)


def show_menu():
    """Shows users menu."""
    choice = None

    while choice != 'q':
        print("Enter 'q' to quit.")
        for key, value in menu.items():
            print('{}) {}'.format(key, value.__doc__))
        choice = input('Action: ').lower().strip()

        if choice in menu:
            menu[choice]()


def add_entry():
    """Add an entry"""
    pass


def view_entries():
    """View previous entries."""
    pass


def delete_entry(entry):
    """Delete an entry."""
    pass


menu = OrderedDict([
    ('a', add_entry),
    ('v', view_entries),
])


if __name__ == '__main__':
    initialize()
    show_menu()
