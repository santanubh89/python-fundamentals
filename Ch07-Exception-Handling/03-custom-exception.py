class InputError(Exception):
    def __init__(self, message, param):
        self.message = message
        self.param = param
        super().__init__(message)

def divide(num, den):
    if num == 0:
        raise InputError('Result will always be 0', num)
    if den == 0:
        raise InputError('Denominator should not be 0', den)
    result = num / den
    return result

try:
    print('Enter the input integers in format x y')
    numerator, denominator = map(int, input().split())
    division = divide(numerator, denominator)
    print(f'Result: {division}')
except InputError as ie:
    print(f'Illegal argument: {ie.message}')
except Exception as e:
    print(f'Something went wrong: {e}')
finally:
    print('Program execution completed')