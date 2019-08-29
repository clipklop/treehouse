a = []

# create the table (name, age, job)
a.append(["Nick", 30, "Doctor"])
a.append(["John",  8, "Student"])
a.append(["Paul", 22, "Car Dealer"])
a.append(["Mark", 66, "Retired"])    

# sort the table by age
import operator
a.sort(key=operator.itemgetter(1))

# print the table
# print(a)


courses = {'count': 2,
           'title': 'Django Basics',
           'prereqs': [{'count': 3,
                     'title': 'Object-Oriented Python',
                     'prereqs': [{'count': 1,
                               'title': 'Python Collections',
                               'prereqs': [{'count':0,
                                         'title': 'Python Basics',
                                         'prereqs': []
                                         }]}]
           }]}
# print(set(courses['prereqs'][0]).issubset(set(courses)))
for key, val in courses.items():
    print(val)
