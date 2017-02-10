import random

my_list = [1, 2, 3, 4, 5]

def nchoices(iter1, num):
    new_list = []
    for _ in range(num):
        get_random = random.choice(iter1)
        new_list.append(get_random)
        
    return new_list

print(nchoices(my_list, ))
