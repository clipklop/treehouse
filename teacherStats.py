# Create a function named most_classes that takes a dictionary of teachers.
# Each key is a teacher's name and their value is a list of classes they've taught.
# most_classes() should return the teacher with the most classes.

# The dictionary will be something like:
# {'Jason Seifer': ['Ruby Foundations', 'Ruby on Rails Forms', 'Technology Foundations'],
#  'Kenneth Love': ['Python Basics', 'Python Collections']}
#
# Often, it's a good idea to hold onto a max_count variable.
# Update it when you find a teacher with more classes than
# the current count. Better hold onto the teacher name somewhere
# too!
#
# Your code goes below here.

teachers = {'Jason Seifer': ['Ruby Foundations', 'Ruby on Rails Forms', 'Technology Foundations'],
  'Kenneth Love': ['Python Basics', 'Python Collections']}

def most_classes(teachers):
  max_count = 0
  max_teacher = ''
  for key in teachers:
    class_count = len(teachers[key])
    if class_count > max_count:
      max_teacher = key
      max_count = class_count
  return max_teacher


# Next, create a function named num_teachers that takes the same dictionary of teachers and classes. 
# Return the total number of teachers.

def num_teachers(teachers):
  teachers_list = 0
  for keys in teachers.keys():
    teachers_list += 1
  return teachers_list


# Now, create a function named stats that takes the teacher dictionary. 
# Return a list of lists in the format [<teacher name>, <number of classes>].
# For example, one item in the list would be ['Dave McFarland', 1].

def stats(teachers):
    teachers_stats = []
    for key, value in teachers.items():
        teachers_list = [key, len(value)]
        teachers_stats.append(teachers_list)
    return teachers_stats


# Great work! Finally, write a function named courses that takes the teachers dictionary.
# It should return a single list of all of the courses offered by all of the teachers.

def courses(teachers):
    courses_list = []
    for key in teachers.values():
        courses_list.extend(key)
    return courses_list
