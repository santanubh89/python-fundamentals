# split
name = 'Foo Bar Baz'
names = name.split(' ')
print(f'Split Parts = {names}, Type = {type(names)}')
f_name, m_name, l_name = name.split(' ')
print(f'First name = {f_name}, Middle Name = {m_name}, Last Name = {l_name}')

# partition
names = name.partition(' ')
print(f'Partitioned Parts = {names}, Type = {type(names)}')

# join
parts = ','.join(names)
print(f'Parts = {parts}')
