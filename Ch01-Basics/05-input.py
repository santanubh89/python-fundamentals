name = input('Enter your name: ')
year_of_birth = input(f'Hello, {name}! Enter your year of birth: ')
print(f'Type of input year of birth: {type(year_of_birth)}')
age = 2025 - int(year_of_birth)
print(f'Age of {name} is: {age}')

# input secrets
import getpass

username = getpass.getpass('Enter your Username: ')
password = getpass.getpass('Enter your Password: ')
print(f'User {username} is now authenticated')