pi_str = '3.14'
pi = float(pi_str)
print(f'Value of Pi = {pi}, initial type = {type(pi_str)}, converted type = {type(pi)}') # str, float

age_in = '30'
age = int(age_in)
print(f'Value of Age = {age}, initial type = {type(age_in)}, converted type = {type(age)}') # str, int

a = '1'
b = '2'
res = a + b
print(f'Added value = {res}') # 12 - string

res = int(a) + int(b)
print(f'Added value = {res}') # 3 - integer

e = 2.71
e_str = str(e)
print(f'Value of E = {e}, initial type = {type(e)}, converted type = {type(e_str)}') # float, str

# Implicit typecasting - Python doing the typecasting
pi = 3.14
n = 10
sum = n + pi
print(f'Value of Sum = {sum}, type = {type(sum)}') # float
