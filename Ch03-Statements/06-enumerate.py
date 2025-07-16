name = 'Foo Bar'
for item in enumerate(name):
    print(f'Item: {item}, Type: {type(item)}')

for index, value in enumerate(name):
    print(f'Index: {index}, Value: {value}')