# Map: Transform a list: store first characters of each word
name_list = ['Foo', 'Bar', 'Baz', 'Charlie', 'Tango']
first_letters = list(map(lambda name: name[0], name_list))
print(f'List of first letters: {first_letters}')

# Filter: Find words with more than a given length
fruits = ['apple', 'banana', 'orange', 'strawberry', 'guava', 'cherry', 'berry']
filtered_fruits = list(filter(lambda fruit: len(fruit) > 5, fruits))
print(f'Fruits with more than 5 letters: {filtered_fruits}')

# Reduce: Sum of all numbers
from functools import reduce
num_list = [5, 1, 9, 7, 3]
sum = reduce(lambda x,y:x+y, num_list, 0)
print(f'Sum of all numbers: {sum}')

# Filter-Map-Reduce: Sum of square of all odd numbers
num_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
sum_of_square = reduce(lambda x,y:x+y, map(lambda x : x * x ,filter(lambda num : num %2 != 0, num_list)), 0)
print(f'Sum of square of all numbers: {sum_of_square}')

# Filtering on a dictionary
students = {'Foo': 92, 'Bar': 65, 'Baz': 80, 'Charlie': 95, 'Tango': 40}
filtered_dictionary = list(filter(lambda pair: pair[1] > 75, students.items()))
print(filtered_dictionary)
