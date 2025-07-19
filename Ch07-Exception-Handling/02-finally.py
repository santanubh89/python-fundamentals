try:
    number = int(input('Enter a number: '))
    a = [6, 3]
    print(f'Result: {a[number]}')
except ValueError as v:
    print(f'Entered number must be an integer: {v}')
except IndexError as i:
    print(f'Index out of bound: {i}')
finally:
    print('Program execution completed')