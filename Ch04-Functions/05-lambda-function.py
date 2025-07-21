from numpy.ma.extras import average


def square(x):
    return x ** 2

square_lambda = lambda x: x ** 2

print(square(5))
print(square_lambda(5))

average = lambda x, y: (x + y) / 2
print(average(1, 2))

def apply(fx, args):
    return - fx(args)

print(apply(square_lambda, 5))