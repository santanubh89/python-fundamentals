name = 'Foo Bar Baz'

name_lower = name.lower()
name_upper = name.upper()
print(f'Actual value = {name}, , is lower case: {name.islower()}, is upper case: {name.isupper()}, is title case: {name.istitle()}')
print(f'Lower case value = {name_lower}, is lower case: {name_lower.islower()}, is upper case: {name_lower.isupper()}')
print(f'Upper case value = {name_upper}, is lower case: {name_upper.islower()}, is upper case: {name_upper.isupper()}')

title = 'introduction to Python'
capitalized_title = title.capitalize() # Converts first character to upper case
print(f'Capitalized title = {capitalized_title}')