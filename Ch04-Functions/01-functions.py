def greet():
    print('Hello from first function!')

greet()

def greet_user(message, user):
    final_message = f'Greeting message to user {user} is {message}'
    print(final_message)

greet_user('Hello', 'Foo')

def prepare_greeting_message(user):
    message = f'Hello, Mr {user}!'
    return message

message = prepare_greeting_message('Foo')
print(f'Message is: {message}')

def add_multiply_numbers(num1, num2):
    """
    :param num1: First number
    :param num2: Second number
    :return: A tuple, consisting of the addition and multiplication
    """
    add = num1 + num2
    multiply = num1 * num2
    return add, multiply

result_tuple = add_multiply_numbers(3, 5)
print(f'Result tuple: {result_tuple}, Type = {type(result_tuple)}')
add, multiply = add_multiply_numbers(3, 5)
print(f'Addition = {add}, Multiplication = {multiply}')

print('Printing documentation of add_multiply_numbers')
help(add_multiply_numbers)