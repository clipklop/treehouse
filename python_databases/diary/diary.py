#!/usr/bin/env python3
"""
    * CLI Diary app
"""


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
    pass


def add_entry():
    """Add an entry"""
    pass


def view_entries():
    """View previous entries."""
    pass


def delete_entry(entry):
    """Delete an entry."""
    pass


if __name__ == '__main__':
    initialize()
    show_menu()
