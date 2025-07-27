import time
from functools import lru_cache

@lru_cache(maxsize=None) # memoize
def complex_function(number):
    print(f"Complex function execution started:: input = {number}")
    time.sleep(3)
    return number ** 2

print(f'Result = {complex_function(3)}')
print(f'Result = {complex_function(3)}')
print(f'Result = {complex_function(10)}')
print(f'Result = {complex_function(3)}')
print(f'Result = {complex_function(3)}')
print(f'Result = {complex_function(10)}')
print(f'Result = {complex_function(7)}')
print(f'Result = {complex_function(3)}')
print(f'Result = {complex_function(7)}')