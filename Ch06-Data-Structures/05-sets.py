num_set = {5, 1, 9, 5, 7, 1, 3, 5}
print(f'Content of set = {num_set}, Type = {type(num_set)}')

print(f'Length of the set: {len(num_set)}')

# Iterate
for num in num_set:
    print(f'Element = {num}')

for index, value in enumerate(num_set):
    print(f'Index = {index}, Value = {value}')

# Check if an element is present
if 7 in num_set:
    print(f'7 is present')
else:
    print(f'7 is not present')

# Set creation
num_set = set()
print(f'Content= {num_set}, Type = {type(num_set)}, Length= {len(num_set)}')
num_set.add(5)
num_set.add(1)
print(f'Content= {num_set}, Type = {type(num_set)}, Length= {len(num_set)}')

# Unique characters in a string
input = 'Mississippi'
unique_chars = set(input)
print(f'Unique characters in {input}: {unique_chars}')