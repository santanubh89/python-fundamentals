def loggable(fx):
    def decorated_func(*args, **kwargs):
        print(f'Processing started: {fx.__name__}')
        fx(*args, **kwargs)
        print(f'Processing finished {fx.__name__}')
        print('-----------------------------------')
    return decorated_func

@loggable
def hello():
    print('Hello, world')

hello()

@loggable
def add(a, b):
    sum = a + b
    print(f'Sum of {a} and {b} is {sum}')

add(10, 20)