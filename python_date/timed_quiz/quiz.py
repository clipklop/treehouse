import datetime
import random

from questions import Add, Multiply


class Quiz:
    questions = []
    answers = []

    def __init__(self):
        question_types = (Add, Multiply)
        # generate 10 different questions with numbers from 1 to 10
        for _ in range(10):
            num1 = random.randint(1, 15)
            num2 = random.randint(1, 15)
            question = random.choice(question_types)(num1, num2)
            self.questions.append(question)
        # add these questions to self.questions
        return

    def take_quiz(self):
        # log the start time
        # ask all of the questions
        # log if they got the questions right
        # log the end time
        # show a summary
        return

    def ask(self, question):
        # log the start time
        # capture the answer
        # check the answer
        # log the end time
        # if the answer's right, send back True
        # otherwise, send back False
        # send back the elapsed time, too
        return

    def total_correct(self):
        # return the total # of correct answers
        return [i for i in self.answers if i[0]]
        # total = 0
        # for answer in self.answers:
        #     if answer[0]:
        #         total += 1
        # return total

    def summary(self):
        # print how many you got right and the total # of questions. 9/10
        # print the total time for the quiz: 30 seconds!
        print(f'You got {self.total_correct} out of \
            {len(self.question)} right.')
        print(f'It took you {(self.end_time-self.start_time).seconds} \
            seconds total.')
