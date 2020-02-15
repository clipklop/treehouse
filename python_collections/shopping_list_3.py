# *
# Version 3 of Shopping List app from Basic course.
# *


import os


# make a list to hold onto our products
shopping_list = []


def clear_screen():
    """ Clear the screen, uses appropriate command for each OS. """
    os.system('cls' if os.name == 'nt' else 'clear')


def show_help():
    """ Print our instrution on how to use the app. """
    clear_screen()
    print("""
        What should we pick up at the store?\n
        Enter 'DONE' or 'QUIT' to stop adding items.
        Enter 'HELP' for this help.
        Enter 'SHOW' to see your current list.
        Enter 'REMOVE' to remove an item from the list.
    """)


def add_to_list(item):
    """ Add new items to our list. """
    show_list()

    if len(shopping_list):
        position = input("Where should I add {}?\n"
            "Press ENTER to add to the end of the list\n"
            "> ".format(item))
    else:
        position = 0

    try:
        position = abs(int(position))
    except ValueError:
        position = None
    if position is not None:
        shopping_list.insert(position - 1, item)
    else:
        shopping_list.append(item)

    show_list()


def show_list():
    """ Print out the list. """
    clear_screen()
    print("Here is your list: ")

    for index, item in enumerate(shopping_list, start = 1):
        print("{}. {}".format(index, item))

    print("-" * 10)


def remove_from_list():
    show_list()
    what_to_remove = input("What would you like to remove?\n> ")
    try:
        shopping_list.remove(what_to_remove)
    except ValueError:
        print("Sorry, no such item in the list.")
    show_list()

show_help()


# ask for new items
while True:
    new_item = input("> ")

    # be able to quit the app
    if new_item.upper() == 'DONE' or new_item.upper() == "QUIT":
        break
    elif new_item.upper() == 'HELP':
        show_help()
        continue
    elif new_item.upper() == 'SHOW':
        show_list()
        continue
    elif new_item.upper() == "REMOVE":
        remove_from_list()
    else:
        add_to_list(new_item)

show_list()