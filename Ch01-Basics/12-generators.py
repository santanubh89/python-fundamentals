def my_generator():
    for i in range(3):
        yield i

gen = my_generator()
print(f'Generated type: {gen}')
print(next(gen))
print(next(gen))
print(next(gen))
# print(next(gen)) # Error - StopIteration

gen.close() # Closes generator

def my_generator():
    for i in range(3):
        yield i

gen = my_generator()
for i in gen:
    print(f'Next value: {i}')