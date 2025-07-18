num_tuple = (5, 1, 9, 7, 3, 7, 9, 7)
print(f'Numbers: {num_tuple}, Type: {type(num_tuple)}')
print(f'Length of tuple: {len(num_tuple)}')

single_element_tuple = (1, )
print(f'Single element tuple: {single_element_tuple}')

print(f'0th element = {num_tuple[0]}')
print(f'1st element = {num_tuple[1]}')
print(f'Last element = {num_tuple[-1]}')

for element in num_tuple:
    print(f'Element in tuple: {element}')

for index, value in enumerate(num_tuple):
    print(f'Index = {index}, Value = {value}')

# Count and Index
count_7 = num_tuple.count(7)
print(f'Count of 7: {count_7}')

index_7 = num_tuple.index(7)
print(f'First index of 7: {index_7}')

# Convert list to tuple
num_list = [5, 1, 9, 7, 3]
num_tuple = tuple(num_list)
print(f'Numbers: {num_tuple}, Type: {type(num_tuple)}')

# tuple concatenation
odd_numbers = (1, 3, 5, 7, 9)
even_numbers = (2, 4, 6, 8)
all_numbers = odd_numbers + even_numbers
print(f'All numbers: {all_numbers}')

# Check if present
if 0 in all_numbers:
    print(f'All numbers 0 found: {all_numbers}')
else:
    print('0 not found in the tuple')