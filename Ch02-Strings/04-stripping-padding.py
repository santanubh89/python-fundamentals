name = 'Foo!!!'
print(f'Stripped (from right) string = {name.rstrip("!")}')

name = '@@@Foo@@@'
print(f'Stripped (from right and left) string = {name.rstrip("@").lstrip("@")}')

print(f'Stripped (all - both right and left) string = {name.strip("@")}')

# center
name = 'Foo'
centred = name.center(10, '*')
print(f'Padded name = {centred}, Length = {len(centred)}')

# multiplying
name = 'Foo'
name_6times = name * 6
print(f'Multiplied name = {name_6times}')