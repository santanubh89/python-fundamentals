name = 'Foo Bar Baz'
print(f'Value of String = {name}, type = {type(name)}')

# Length
print(f'Length of the string = {len(name)}')

# Index
print(f'0th element of the string = {name[0]}')
print(f'4th element of the string = {name[4]}')
print(f'Last element of the string = {name[-1]}')
print(f'Last 3rd element of the string = {name[-3]}')

# iteration
f_name = 'Foo'
for char in f_name:
    print(f'Character = {char}')

for index, char in enumerate(f_name):
    print(f'Index = {index}, Character = {char}')

# count
count_a = name.count('a')
count_r = name.count('r')
print(f'Count of a = {count_a}, Count of r = {count_r}')

# concatenation
f_name = 'Foo'
l_name = 'Bar'
full_name = f'{f_name} {l_name}'
print(f'Full Name = {full_name}')

full_name = f_name + ' ' + l_name
print(f'Full Name = {full_name}')

full_name = f_name.__add__(' ').__add__(l_name)
print(f'Full Name = {full_name}')
