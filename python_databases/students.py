#


import peewee as pw


DB = pw.SqliteDatabase('students.db')

STUDENTS = [
    {'username': 'mischa',
     'points': 46999},
    {'username': 'kenneth',
     'points': 6111},
    {'username': 'chalkers',
     'points': 777},
    {'username': 'craigden',
     'points': 3333},
    {'username': 'davemcfarland',
     'points': 16617},
]


class Student(pw.Model):
    username = pw.CharField(max_length=255, unique=True)
    points = pw.IntegerField(default=0)

    class Meta:
        database = DB


def add_student(students):
    for student in students:
        try:
            Student.create(
                username=student['username'], points=student['points'])
        except pw.IntegrityError:
            student_record = Student.get(username=student['username'])
            student_record.points = student['points']
            student_record.save()


def top_student():
    student = Student.select().order_by(Student.points.desc()).get()
    return student


if __name__ == '__main__':
    DB.connect()
    DB.create_tables([Student], safe=True)
    add_student(STUDENTS)
    print("Our top student right now is: '{0.username}'!".format(
        top_student()))
