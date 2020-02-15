import datetime


now = datetime.datetime.now()

print(now.strftime('%B %d'))
print(now.strftime('%d.%m.%Y'))

birthday = datetime.datetime.strptime('25.08.2020', '%d.%m.%Y')
print(birthday)
