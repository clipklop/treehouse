

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
