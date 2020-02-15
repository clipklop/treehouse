"""
    * Tasks from Regex exercises
"""
import re


# Create a function named find_words that takes a count and a string.
# Return a list of all of the words in the string that are count
# word characters long or longer.

# EXAMPLE:
# >>> find_words(4, "dog, cat, baby, balloon, me")
# ['baby', 'balloon']
def find_words(i, s):
    # return [x for x in re.findall(r'\w+', s) if len(x) >= i]
    return re.findall(r'\w{{{},}}'.format(i), s)  # you've to escape brackets


# print(find_words(4, "dog, cat, baby, balloon, me"))


string = 'Perotto, Pier Giorgio'
names = re.match(r'(?P<Last>\w+),\s(?P<Name>[\w ]+)', string)
# print(names)


string = '''Love, Kenneth, kenneth+challenge@teamtreehouse.com, 555-555-5555, @kennethlove
Chalkley, Andrew, andrew@teamtreehouse.co.uk, 555-555-5556, @chalkers
McFarland, Dave, dave.mcfarland@teamtreehouse.com, 555-555-5557, @davemcfarland
Kesten, Joy, joy@teamtreehouse.com, 555-555-5558, @joykesten'''

contacts = re.findall(r'''
    #(?P<name>[-\w,. ]+),\s
    (?P<email>[-+\w ]+@[-\w\d.]+),\s
    (?P<phone>\d{3}-\d{3}-\d{4}),\s#\(?\d+\)?\-?)
    # (?P<twitter>@\w+)
''', string, re.X | re.I | re.M)

twitters = re.search(r'''
    (?P<twitter>@\w+)$
''', string, re.X | re.I | re.M)
# print(twitters)
