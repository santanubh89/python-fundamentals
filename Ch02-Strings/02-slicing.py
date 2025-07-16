name = 'Foo Bar Baz'
name_copy = name[0:]
print(f'Copied string = {name_copy}')

print(f'First 5 characters = {name[0:5]}')

first_space_index = name.index(' ')
first_name = name[:first_space_index]
print(f'First name = {first_name}')

reversed_name = name[::-1]
print(f'Reversed name = {str(reversed_name)}')

# find
pos_B = name.find('B')
print(f'B is present at position = {pos_B}')