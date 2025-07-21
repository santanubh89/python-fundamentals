x = 10
y = 20/2
z = x

print(f'X == Y: {x == y}') # True
print(f'X is Y: {x is y}') # False

print(f'X == X: {x == z}') # True
print(f'X is X: {x is z}') # True


list_1 = [1, 2, 3]
list_2 = [1, 2, 3]
list_3 = list_1
print(f'list_1 == list_2: {list_1 == list_2}') # True
print(f'list_1 is list_2: {list_1 is list_2}') # False

print(f'list_1 == list_3: {list_1 == list_3}') # True
print(f'list_1 is list_3: {list_1 is list_3}') # True

print(f'Location of X = {id(x)}')
print(f'Location of Y = {id(y)}')
print(f'Location of Z = {id(z)}')