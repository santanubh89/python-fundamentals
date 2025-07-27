import time


def list_to_string_1(n):
    return [str(num) for num in range(n)]

def list_to_string_2(n):
    return list(map(str, range(n)))

start_time = time.time()
result_1 = list_to_string_1(10000000)
print(f'Time taken by option 1: {time.time() - start_time}') # seconds

start_time = time.time()
result_2 = list_to_string_1(10000000)
print(f'Time taken by option 2: {time.time() - start_time}') # seconds

import timeit
statement = '''
list_to_string_1(100)
'''
setup = '''
def list_to_string_1(n):
    return [str(num) for num in range(n)]
'''
elapsed = timeit.timeit(stmt=statement, setup=setup, number=1000000)
print(f'Time taken by option 1: {elapsed}')

statement = '''
list_to_string_2(100)
'''
setup = '''
def list_to_string_2(n):
    return list(map(str, range(n)))
'''
elapsed = timeit.timeit(stmt=statement, setup=setup, number=1000000)
print(f'Time taken by option 2: {elapsed}')