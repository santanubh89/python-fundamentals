# range function
for n in range(3):
    print(f'Number: {n}') # 0 1 2

# iterating string
name = 'Foo'
for char in name:
    print(f'Character: {char}')

# iterating list
num_list = [1, 2, 3]
index = 0
for num in num_list:
    print(f'Index = {index}, Number: {num}')
    index += 1

# calculating sum
num_list = [1, 2, 3]
sum = 0
for num in num_list:
    sum += num
print(f'Sum = {sum}')

# tuple
tup = ('foo', 'bar', 'baz')
for name in tup:
    print(f'Name in tuple: {name}')

# enumerate function
for index, value in enumerate(tup):
    print(f'Index: {index}, Value: {value}')

# dict
numbers = {1: 'ONE', 2: 'TWO', 3: 'THREE'}
for key in numbers:
    print(f'Key: {key}, Value: {numbers[key]}')

for key, value in numbers.items():
    print(f'Key: {key}, Value: {value}')

# break - linear search
input_array = [5, 1, 9, 7, 3]
search_num = 7
index = 0
position = -1
for num in input_array:
    if input_array[index] == search_num:
        position = index
        break
    index += 1
if position == -1:
    print(f'{search_num} not found in the array')
else:
    print(f'{search_num} found in position {position}')

# continue - find sum of odd numbers
num_list = list(range(10))
sum = 0
for num in num_list:
    if num % 2 == 0:
        continue
    sum += num
print(f'Sum of odd numbers= {sum}')

# pass - do nothing
for num in num_list:
    pass