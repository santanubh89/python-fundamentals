# Factorial
def factorial(n):
    if n in (0, 1):
        return 1
    else:
        return n * factorial(n - 1)


fact = factorial(6)
print(f'Factorial of 6 = {fact}')

# Fibonacci Series
def fibonacci(n):
    fib_series = []
    a, b = 0, 1
    for _ in range(n):
        fib_series.append(a)
        a, b = b, a + b
    return fib_series

result = fibonacci(10)
print(f'Fibonacci of 10 = {result}')