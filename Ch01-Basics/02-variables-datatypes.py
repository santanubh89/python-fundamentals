# String
user_name = 'Foo'
print(f'String value = {user_name}, type = {type(user_name)}') # type = <class 'str'>

# Integer
user_age = 35
print(f'Integer value = {user_age}, type = {type(user_age)}') # type = <class 'int'>

# Float
pi = 3.14
print(f'Float value = {pi}, type = {type(pi)}') # type = <class 'float'>

# Boolean
is_active = True
print(f'Float value = {is_active}, type = {type(is_active)}') # type = <class 'bool'>

# NoneType
address = None
print(f'NoneType value = {address}, type = {type(address)}') # type = <class 'NoneType'>

# sum of int and float is a float
result = user_age + pi
print(f'Float value = {result}, type = {type(result)}') # type = <class 'float'>

# complex number
complex_data = 1+2j
print(f'Complex value = {complex_data.real}, {complex_data.imag}, type = {type(complex_data)}') # type = <class 'complex'>

# list
list = [1, 2, 3.14, 10, 'foo']
print(f'List value = {list}, type = {type(list)}') # type = <class 'list'>

# dict
num_map = {1: 'one', 2: 'two', 3: 'three'}
print(f'Dictionary value = {num_map}, type = {type(num_map)}') # type = <class 'dict'>

# int => whole numbers => 3, 50, 170
# float => decimal numbers => 2.3, 3.14, 17.05
# str => ordered sequence of characters => "hello", 'world', "2500"
# list => ordered sequence of other types => [10, "hello", 200.3, True]
# dict => key value pairs => {"key1" : "value1", "key2" : "value2"}
# tup => ordered immutable sequence of other types => (10, "hello", 200.3, True)
# set => unordered collection of unique objects => {"a", "b"}
# bool => logical true or false => True | False