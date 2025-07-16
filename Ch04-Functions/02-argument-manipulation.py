def greet(name = 'user'):
    print(f'Hello, {name}')

greet() # Hello, user
greet('Foo') # Hello, Foo

def print_user(name, experience = 0, skill = 'Java'):
    print(f'{name} has {experience} years of experience in {skill}')

print_user('Foo') # Foo has 0 years of experience in Java
print_user('Bar', 10) # Bar has 10 years of experience in Java
print_user('Baz', 12, 'Python') # Baz has 12 years of experience in Python