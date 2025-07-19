numerator = int(input('Enter the numerator: '))
denominator = int(input('Enter the denominator: '))
try:
    division = numerator / denominator
    print(f'Division result: {division}')
except ZeroDivisionError:
    print('Error in input: cannot divide by zero')