name = 'Foo Bar'
age = 30

message = f'Hello, {name}. You are {age} years old.'
print('Format 1: '+message)

message = 'Hello, {}. You are {} years old.'.format(name, age)
print('Format 2: '+message)

template = 'The {} {} {}'
print(template.format('quick', 'brown', 'fox'))

template = 'The {2} {0} {1}'
print(template.format('brown', 'fox', 'quick'))

template = 'The {q} {b} {f}'
print(template.format(b='brown', f='fox', q='quick'))