import random

random_int = random.randint(0, 100)
print(f'Random int: {random_int}')

random.seed(101)
random_int = random.randint(0, 100)
print(f'Random int: {random_int}')
my_list = list(range(0, 20))
random.shuffle(my_list)
print(my_list)
print(random.choice(my_list))
print(random.choice(my_list))
print(random.choice(my_list))

# Sample with replacement
choices = random.choices(population=my_list, k=10)
print(f'Element can be present twice = {choices}')

choices = random.sample(population=my_list, k=10)
print(f'Element cant be present twice = {choices}')