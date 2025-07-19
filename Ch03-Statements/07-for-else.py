for i in range(5):
    print(i)
else:
    print('Loop is over')

for i in range(5):
    print(i)
    if i == 2:
        break
else:
    print('Will not be executed')