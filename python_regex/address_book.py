"""
    * Task # 1: Address Book
"""
import re


with open('names.txt', 'r') as names:
    data = names.read()
    # print(re.match(r'Love,', names.read()))
    # print(re.search(r'Obama,', names.read()))
# print(re.match(r'Love,', data))
# print(re.search(r'Obama,', data))

print(re.search(r'\w, \w', data))
print(re.search(r'\(\d\d\d\)', data))
