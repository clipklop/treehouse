# # my_list = [1, 2, 3]
# # my_list.append(4)
# # my_list.extend([5, 6, 7, 8])

# # strings = 'hello there students'.split()
# # colons = 'red:blue:green'.split(":")

# # flavors = ['choco', 'mint', 'strawberry']

# # sentence = "My favorite flavors are {}".format(', '.join(flavors))

# # available = "banana split;hot fudge;cherry;malted;black and white"
# # sundaes = available.split(";")
# # menu = "Our available flavors are: {}."
# # icecreams = ", ".join(sundaes)
# # menu = "Our available flavors are: {}.".format(icecreams)

# # # print(menu)

# # for letter in "abcdefghijklmnopqrstuvwxyz":
# #     print(letter.upper())

# # def squared(num):
# #     try:
# #         num = int(num)
# #         return num * num
# #     except ValueError:
# #         return num * len(num)

# # print(squared('5'))

# # import random

# # def even_odd(num):
# #     # If % 2 is 0, the number is even.
# #     # Since 0 is falsey, we have to invert it with not.
# #     return not num % 2

# # def even_random():
# #     start = 5
# #     while start > 0:
# #         rand = random.randint(1, 99)
# #         if even_odd(rand):
# #             print("{} is even".format(rand))
# #         else:
# #             print("{} is odd".format(rand))
# #         start -= 1

# # print(even_random())

# the_list = ["a", 2, 3, 1, False, [1, 2, 3]]

# # Your code goes below here
# the_list.insert(0, the_list.pop(3))
# the_list.remove("a")
# the_list.remove(False)
# the_list.remove([1, 2, 3])
# the_list.extend(range(4, 21))

# You can check for dictionary membership using the
# "key in dict" syntax from lists.

# ### Example
# my_dict = {'apples': 1, 'bananas': 2, 'coconuts': 3}
# my_list = ['apples', 'coconuts', 'grapes', 'strawberries']
# # members(my_dict, my_list) => 2
# def members(my_dict, my_list):
#     count = 0
#     for key in my_dict:
#         if key in my_list:
#             count += 1
#     return count

# print(members(my_dict, my_list))

# E.g. word_count("I am that I am") gets back a dictionary like:
# {'i': 2, 'am': 2, 'that': 1}
# Lowercase the string to make it easier.
# Using .split() on the sentence will give you a list of words.
# In a for loop of that list, you'll have a word that you can
# check for inclusion in the dict (with "if word in dict"-style syntax).
# Or add it to the dict with something like word_dict[word] = 1
# def word_count(my_string):
#     list_string = my_string.lower().split(" ")
#     list_dict = {}
#     for key in list_string:
#         if key in list_dict:
#             list_dict[key] += 1
#         else:
#             list_dict[key] = 1
#     return list_dict

# word_count("I am That I am")

# Create a function named string_factory that accepts a list of dictionaries and a string.
# Return a new list build by using .format() on the string,
 # filled in by each of the dictionaries in the list.
# dicts = [
#     {'name': 'Michelangelo',
#      'food': 'PIZZA'},
#     {'name': 'Garfield',
#      'food': 'lasanga'},
#     {'name': 'Walter',
#      'food': 'pancakes'},
#     {'name': 'Galactus',
#      'food': 'worlds'}
# ]

# string = "Hi, I'm {name} and I love to eat {food}!"
# def string_facory(dicts, string):
#     my_list = []
#     for dict in dicts:
#         my_list.append(string.format(**dict))
#     return my_list

# print(string_facory(dicts, string))


# Create a function named most_classes that takes a dictionary of teachers.
# Each key is a teacher's name and their value is a list of classes they've taught.
# most_classes should return the teacher with the most classes.

# The dictionary will be something like:
# my_dict = {'Jason Seifer': ['Ruby Foundations', 'Ruby on Rails Forms', 'Technology Foundations'], 'Kenneth Love': ['Python Basics', 'Python Collections']}
# #
# # Often, it's a good idea to hold onto a max_count variable.
# # Update it when you find a teacher with more classes than
# # the current count. Better hold onto the teacher name somewhere
# # too!

# def most_classes(my_dict):
#     max_count = 0
#     teachers_name = ''
#     for keys in my_dict:
#         if len(my_dict[keys]) > max_count:
#             max_count = len(my_dict[keys])
#             teachers_name = keys
#     return teachers_name

# print(most_classes(my_dict))


# Create a function named combo() that takes two iterables and returns a list of tuples.
# Each tuple should hold the first item in each list, then the second set,
# then the third, and so on. Assume the iterables will be the same length.

# combo([1, 2, 3], 'abc')
# Output:
# [(1, 'a'), (2, 'b'), (3, 'c')]
# If you use .append(), you'll want to pass it a tuple of new values.
# def combo(iter1, iter2):
#     my_list = []
#     for index, value in enumerate(iter2):
#         my_tuple = iter1[index], value
#         my_list.append(my_tuple)
#     print(my_list)

# combo([1, 2, 3], 'abc')


### DECORATORS

# def gen_and_print(text):
#     print("Start!")
#     yield
#     print(text)

# s = gen_and_print('Hi!')
# next(s)
# next(s)
# # print(s)

# def counter(func):
#     inner_counter = 0
#     def inner(*args, **kwargs):
#         nonlocal inner_counter
#         print("Counter", inner_counter)
#         inner_counter += 1
#         func(*args, **kwargs)

#     return inner

# @counter
# def next_letter(prev):
#         return chr(prev + 1)

# for i in range(10):
#     print(next_letter(65 + i))

# Example:
# values = [{"name": "Michelangelo", "food": "PIZZA"}, {"name": "Garfield", "food": "lasagna"}]
# string_factory(values)
# ["Hi, I'm Michelangelo and I love to eat PIZZA!", "Hi, I'm Garfield and I love to eat lasagna!"]

# values = [{"name": "Michelangelo", "food": "PIZZA"}, {"name": "Garfield", "food": "lasagna"}]
# template = "Hi, I'm {name} and I love to eat {food}!"

# def string_factory(dict):
#     tmp = []
#     for value in dict:
#         tmp.append(template.format(**value))
#     return tmp

# print(string_factory(values))
# print(template)

# E.g. word_count("I do not like it Sam I Am") gets back a dictionary like:
# {'i': 2, 'do': 1, 'it': 1, 'sam': 1, 'like': 1, 'not': 1, 'am': 1}
# Lowercase the string to make it easier.

# def word_count(string):
#     parse = string.lower().split()
#     my_dict = {}
#     for word in parse:
#         if word in my_dict:
#             my_dict[word] += 1
#         else:
#             my_dict[word] = 1

#     return my_dict

# print(word_count("I do not like it Sam I Am"))

# The dictionary will look something like:
# {'Andrew Chalkley': ['jQuery Basics', 'Node.js Basics'],
#  'Kenneth Love': ['Python Basics', 'Python Collections']}
#
# Each key will be a Teacher and the value will be a list of courses.
#
# dicts = {'Andrew Chalkley': ['jQuery Basics', 'Node.js Basics', 'AS'], 'Kenneth Love': ['Python Basics', 'Python Collections']}

# def num_teachers(dicts):
#     return len(dicts.keys())

# def num_courses(dicts):
#     total = 0
#     for course in dicts:
#         total += len(dicts[course])
#     return total

# def courses(dicts):
#     courses_list = []
#     for course in dicts.values():
#         courses_list += course
#     return courses_list

# # most_courses should return the name of the teacher with the most courses.
# # You might need to hold onto some sort of max count variable.
# def most_courses(dicts):
#     max_count = 0
#     name = ""
#     for course in dicts:
#         if len(dicts[course]) > max_count:
#             max_count = len(dicts[course])
#             name = course
#     return name

# # I want you to create a function named stats and it'll take our teacher dictionary as its only argument.
# # stats should return a list of lists where the first item in each inner list is the teacher's name
# # and the second item is the number of courses # that teacher has.
# # For example, it might return: [["Kenneth Love", 5], ["Craig Dennis", 10]]
# def stats(dicts):
#     teachers_list = []

#     for teacher in dicts:
#         # teachers_list.append(teacher)
#         # course_len.append(dicts[teacher])
#         # teachers_list += course_len
#         tmp = [teacher, len(dicts[teacher])]
#         teachers_list.append(tmp)
#     print(teachers_list)

# stats(dicts)

# def multiply(*args):
#     first_tuple = args[0]
#     for arg in args[1:]:
#         first_tuple *= arg
#     return first_tuple

# print(multiply(4, 4,4 ))

### 1
# So, first, write a function named covers that accepts a single parameter, a set of topics.
# Have the function return a list of courses from COURSES where the supplied set and the
# course's value (also a set) overlap. For example, covers({"Python"}) would return ["Python Basics"].
### 2
# OK, let's create something a bit more refined. Create a new function named covers_all that takes a
# single set as an argument. Return the names of all of the courses, in a list, where all of the
# topics in the supplied set are covered. For example, covers_all({"conditions", "input"})
# would return ["Python Basics", "Ruby Basics"]. Java Basics and PHP Basics would
# be exclude because they don't include both of those topics.

# COURSES = {
#     "Python Basics": {"Python", "functions", "variables",
#                       "booleans", "integers", "floats",
#                       "arrays", "strings", "exceptions",
#                       "conditions", "input", "loops"},
#     "Java Basics": {"Java", "strings", "variables",
#                     "input", "exceptions", "integers",
#                     "booleans", "loops"},
#     "PHP Basics": {"PHP", "variables", "conditions",
#                    "integers", "floats", "strings",
#                    "booleans", "HTML"},
#     "Ruby Basics": {"Ruby", "strings", "floats",
#                     "integers", "conditions",
#                     "functions", "input"}
# }

# def covers(set_topics):
#     list_topics = []
#     for key, value in COURSES.items():
#         if value & set_topics:
#             list_topics.append(key)
#     return list_topics
# print(covers({"Python"}))

# ### 2
# def covers_all(set_topics):
