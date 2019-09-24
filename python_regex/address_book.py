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

# print(re.findall(r'\w*, \w+', data))
# print(re.findall(r'\(?\d{3}\)? \d{3}-\d{4}', data))

email_check = re.findall(r'[-\w\d+.]+@[-\w\d.]+', data)
# print(email_check)

treehouse = re.findall(r'\b[(team)?trehous]{9,13}\b', data, re.I)

# print(treehouse)


nogov = re.findall(r'''
    [-\w\d+.]+@[-\w\d.]*[^gov\t]+
''', data, re.X | re.I)  # stand for verbose
# print(nogov)


names_position = re.findall(r"""
    \b[-\w]*,  # Find a word boundary, 1+ hyphens or characters, coma
    \s         # Find a whitespace
    [-\w ]+    # 1+ hyphens and chars and explicit spaces
    [^\t\n]    # Ignore tabs and newlines
""", data, re.X)
# print(names_position)


# this is gets real powerful!
# spend hours for searching for a re.finditer thing :D
find_all = re.finditer(r"""
    ^(?P<name>[\w ]*,\s[-\w]+)\t                # Last and first names
    (?P<email>[-\w\d.+]+@[-\w\d.]+)\t           # Email
    (?P<phone>\(?\d{3}\)?-?\s?\d{3}-\d{4})?\t   # Phone
    (?P<job>[\w\s]+,\s[\w\s.]+)\t?              # Job and company
    (?P<twitter>@[\w\d]+)?$                     # Twitter
""", data, re.X | re.M | re.I)
# print([x.groupdict() for x in find_all])


"""
    * re.compile(pattern, flags) - method to pre-compile and save a regular expression pattern, and any associated flags, for later use.
    * .groupdict() - method to generate a dictionary from a Match object's groups. The keys will be the group names. The values will be the results of the patterns in the group.
    * re.finditer() - method to generate an iterable from the non-overlapping matches of a regular expression. Very handy for for loops.
    * .group() - method to access the content of a group. 0 or none is the entire match. 1 through how ever many groups you have will get that group. Or use a group's name to get it if you're using named groups.
"""
compile_line = re.compile(r"""
    ^(?P<name>(?P<last>[\w ]*),\s(?P<first>[-\w]+))\t                # Last and first names
    (?P<email>[-\w\d.+]+@[-\w\d.]+)\t           # Email
    (?P<phone>\(?\d{3}\)?-?\s?\d{3}-\d{4})?\t   # Phone
    (?P<job>[\w\s]+,\s[\w\s.]+)\t?              # Job and company
    (?P<twitter>@[\w\d]+)?$                     # Twitter
""", re.X | re.M | re.I)

print(compile_line.search(data).groupdict())

# print([line.group('name') for line in compile_line.finditer(data)])

for match in compile_line.finditer(data):
    print('{first} {last} <{email}>'.format(**match.groupdict()))
