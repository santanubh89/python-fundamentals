num_list = [5, 1, 9, 7, 3]
print(f'List = {num_list}, Type = {type(num_list)}')

print(f'Length of the array: {len(num_list)}')

print(f'0th element = {num_list[0]}')
print(f'1st element = {num_list[1]}')
print(f'Last element = {num_list[-1]}')

# Iterate
for num in num_list:
    print(f'Element = {num}')

for index, value in enumerate(num_list):
    print(f'Index = {index}, Value = {value}')

# Add elements to the list
num_list.append(0)
print(f'Last element after appending = {num_list[-1]}')

# Replace element in a position
num_list[2] = -9
print(f'Updated element after replace = {num_list[2]}')

# Position of a specific element
pos = num_list.index(-9)
print(f'Position of -9: {pos}')

# Check if an element is present
if 7 in num_list:
    print(f'7 is present at: {num_list.index(7)}')
else:
    print(f'7 is not present')

sub_num_list = num_list[2:5]
print(f'Original List: {num_list}, Sub List: {sub_num_list}')