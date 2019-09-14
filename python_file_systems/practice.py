import unicodedata
import datetime
import os
import re


#  (2012-12-22), (12-22-2012) returns 2012-12-22 dir
def create_daily_dir(string):
    temp = string.split('-')
    if len(temp[0]) == 2:
        temp[0], temp[1], temp[2] = temp[2], temp[0], temp[1]
        print(temp)
    return '-'.join(temp)
# print(create_daily_dir('2012-12-22'))
# print(create_daily_dir('12-22-2012'))
# print(create_daily_dir("04-22-2017"))


# Task: Consistency

# Filenames consist of a username (alphanumeric, 3-12 characters)
# and a date (four digit year, two digit month, two digit day),
# and an extension. They should end up in the format
# year-month-day-username.extension.

# Example: kennethlove2-2012-04-29.txt becomes 2012-04-29-kennethlove2.txt

def cleanup(path):
    os.chdir(path)
    dir_structure = os.listdir(path)
    temp_lst = []
    temp_str = ''
    for f in dir_structure:
        temp_str += '-'.join(re.findall(r'\b\d{2,}\b', f))
        temp_str += '-'
        temp_str += re.findall(r'\b[\w]+\b', f)[0]
        temp_str += re.findall(r'[\.\w]{4,5}$', f)[0]

        # if os.path.isfile(f):
        #     os.renames(f, temp_str)
        temp_lst.append(temp_str)
        temp_str = ''
    return temp_lst


# print(cleanup('/home/clipklop/Templates/kenguroo'))


# working solution
def cleanup1(path):
    for name in os.listdir(path):
        # find the date in the pre-formatted file name
        orig_date = re.search(r'\d{4}-\d{2}-\d{2}', name)
        # format the date correctly
        formatted_date = datetime.datetime.strptime(orig_date.group(), '%Y-%m-%d').date()
        # the file extension is the last 4 characters (i.e. .txt)
        ext = str(name[-4:])
        # concatenate new string as date with a dash plus username plus extension
        # username is found by slicing name up to index of dash (start of date)
        new_str = str(formatted_date) + "-" + str(name[:name.index('-')]) + ext
        # rename files, make sure to join path with file name 
        # os.rename(os.path.join(path, name), os.path.join(path, new_str)) 
        print(os.path.join(path, name), os.path.join(path, new_str)) 

# cleanup1('/home/clipklop/Templates/kenguroo')


# This challenge is a bit different from others you've probably done,
# so try to approach it with an open, creative mind. I made a slugify
# function in the last video, but that is just one approach to making a slug.
# I want you to make your own slugify function in slug.py. Your function
# should accept two arguments, a string to make into an acceptable file or
# directory name, and a path. The rules? Slugs should be unique for their path
# (you can't have two files or directories with the same name in the same directory),
# slugs shouldn't have spaces in them, and slug should start with a number,
# letter, or underscore. Other than that, it's up to you!
def slugify(string, path):
    string = unicodedata.normalize('NFKC', string)
    string = re.sub(r'[^\w\s]', '', string)
    string = re.sub(r'[_\-\s]+', '_', string)
    string = re.sub(r'^[\d]', '', string).strip().lower()

    slug = os.path.join(path, string)

    try:
        os.makedirs(slug)
    except FileExistsError:
        print("Soz, '{}' has already exist. Pick another file name.".format(slug))

    return slug


print(slugify('1as-sd', '/home/clipklop/Templates/kenguroo'))
# print(slugify('as-s1d_'))
# print(slugify('as-sd_'))
# print(slugify('  as-sd_', '/home/clipklop/Templates/kenguroo'))

