from sys import api_version

num_list = [5, 1, 9, 3]

# Add element at the end
num_list.append(7)
print(f'List after append: {num_list}')

# Add element at a specific position
num_list.insert(2, -5)
print(f'List after insert: {num_list}')

# Remove element from the end
num_list.pop()
print(f'List after pop: {num_list}')

# Remove a specific element
num_list.remove(-5)
print(f'List after remove: {num_list}')

# Sort the list
num_list.sort()
print(f'List after sort: {num_list}')

num_list.sort(reverse=True)
print(f'List after sort: {num_list}')

# Reverse the list
num_list.reverse()
print(f'List after reverse: {num_list}')

# Find element at an index
element = num_list.index(5)
print(f'Element at position 2: {element}')

# Count occurrence of an element
name_list = ['Foo', 'Bar', 'Baz', 'Bar']
bar_count = name_list.count('Bar')
print(f'Count of \'bar\': {bar_count}')

# Copy a list
new_names = name_list.copy()
print(f'New names list: {new_names}')

# Merge two lists
num_list = [1, 3, 5, 7, 9]
new_nums = [0, 2, 4, 6, 8]
all_numbers = num_list + new_nums
print(f'Concatenated list: {all_numbers}')
num_list.extend(new_nums)
print(f'Merged list: {num_list}')

# sum, max, min
num_list = [5, 1, 9, 7, 3]
print(f'Sum of numbers in the list: {sum(num_list)}')
print(f'Highest number in the list: {max(num_list)}')
print(f'Smallest number in the list: {min(num_list)}')

# Join elements in the list
letters = ['A', 'B', 'C', 'D', 'E', 'F']
output_str = ', '.join(letters)
print(f'Output string: {output_str}')
