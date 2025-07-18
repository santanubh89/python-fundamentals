num_list = [i for i in range(10)]

print(f'List created using comprehension: {num_list}')

odd_squares = [i * i for i in num_list if (i%2 != 0)]
print(f'Square of odd numbers: {odd_squares}')