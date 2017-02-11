# combo([1, 2, 3], 'abc')
# Output:
# [(1, 'a'), (2, 'b'), (3, 'c')]
# If you use .append(), you'll want to pass it a tuple of new values.

def combo(a, b):
  tuples_list = []
  for key, value in enumerate(a):
    tupy = b[key], value
    tuples_list.append(tupy)
  return tuples_list

# def combo(iterable_1, iterable_2):
#     list_of_tuples = []
#     count = 0
#     for item in iterable_1:
#         list_of_tuples.append((iterable_1[count], iterable_2[count]))
#         count += 1
#     return list_of_tuples

print(combo([1, 2, 3], 'abc'))