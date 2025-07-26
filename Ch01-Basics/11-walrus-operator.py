a = True
print(a)

print(a:=False)

numbers = [1, 2, 3, 4, 5]
while (n := len(numbers)) > 0:
    print(f'Number: {numbers.pop()}')

names = ['Foo', 'Bar', 'Baz']
if (name := input('What is your name?')) in names:
    print(f'Hello, {name}. You can enter!')
else:
    print(f'Sorry, {name}. You are not authorized!')

# Without Walrus:
foods = list()
while True:
    food = input('Enter a food: ')
    if food == 'quit':
        break
    foods.append(food)
print(f'Foods: {foods}')

# With Walrus
foods = list()
while (food := input('Enter a food: ')) != 'quit':
    foods.append(food)
print(f'Foods: {foods}')