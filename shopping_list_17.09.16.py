# make a list to hold onto our products
shopping_list = []

# print our instrution on how to use the app
def show_help():
    print("What should we pick up at the store?")
    print("""
    Enter 'DONE' to stop adding items.
    Enter 'HELP' for this help.
    Enter 'SHOW' to see your current list.
    """)

# print out the list
def show_list():
    print("Here is your list: ")

    for item in shopping_list:
        print(item)

def add_to_list(new_item):
    # add new items to our list
    shopping_list.append(new_item)
    print("Added {}. List now has {} items.".format(new_item, len(shopping_list)))

show_help()

# ask for new items
while True:
    new_item = input("> ")

    # be able to quit the app
    if new_item == 'DONE':
        break
    elif new_item == 'HELP':
        show_help()
        continue
    elif new_item == 'SHOW':
        show_list()
        continue

    add_to_list(new_item)

show_list()