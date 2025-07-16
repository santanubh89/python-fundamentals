# args
def calculate_average(*numbers):
    print(f'Numbers: {numbers}, Type: {type(numbers)}')
    return sum(numbers) / len(numbers)

print(f'Average of 3 numbers: {calculate_average(5, 7, 12)}')
print(f'Average of 5 numbers: {calculate_average(2, 5, 1, 7, 12)}')

# kwargs
def process_order(**kwargs):
    print(f'Items: {kwargs}, Type: {type(kwargs)}')
    if 'fruit' in kwargs:
        print(f'Fruits ordered = {kwargs["fruit"]}')
    else:
        print('No fruits ordered')
    if 'vegetable' in kwargs:
        print(f'Vegetables ordered = {kwargs["vegetable"]}')
    else:
        print('No vegetables ordered')
    if 'beverage' in kwargs:
        print(f'Beverages ordered = {kwargs["beverage"]}')
    else:
        print('No beverages ordered')

process_order(fruit = 'apple', vegetable = 'lettuce')
process_order(beverage = 'soda', vegetable = 'papaya')

# args and kwargs
def my_func(*args, **kwargs):
    print(f'args: {args}, type: {type(args)}')
    print(f'kwargs: {kwargs}, type: {type(kwargs)}')
    print(f'I want {args[0]} {kwargs["food"]}s')

my_func(5, 10, 15, fruit = 'Apple', food = 'Bread', animal = 'Dog')