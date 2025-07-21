def welcome():
    print('Welcome to Python Modules')

result = 10

print(f'Module name = {__name__}')
#__main__ when run directly
#my_module when run from another module

if __name__ == '__main__':
    welcome()