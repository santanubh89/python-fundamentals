x = 1
y = 2

def print_x():
    x = 10
    return x

result = print_x()
print(f'Global X = {x}, Local X = {result}')

def print_y():
    global y
    y = 5
    return y

result = print_y()
print(f'Global Y = {y}, Local Y = {result}')

name = 'GLOBAL'
def greet():
    name = 'ENCLOSING'
    def hello():
        name = 'LOCAL'
        print(f'Hello {name}')
    hello()
greet()