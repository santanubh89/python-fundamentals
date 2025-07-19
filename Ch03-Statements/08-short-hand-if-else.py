a = int(input('Enter A: '))
b = int(input('Enter B: '))
print('A') if a > b else print('AB') if a == b else print('B')

c = 0 if a > b else 1
print(f'C: {c}')