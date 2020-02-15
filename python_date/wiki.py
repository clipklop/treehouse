import datetime


answer_format = '%d.%m'
link_format = '%b_%d'
link = 'https://en.wikipedia.org/wiki/{}'

while True:
    answer = input('What date would you like? ')
    if answer.lower() == 'quit':
        break

    try:
        date = datetime.datetime.strptime(answer, answer_format)
        output = link.format(date.strftime(link_format))
        print(output)
    except ValueError:
        print("That's not a valid date")
