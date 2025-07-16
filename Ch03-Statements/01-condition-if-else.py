age = 20
if age >= 18:
    print('You are eligible to drive')

license = True
if age > 18 and license:
    print('You are eligible to drive')
else:
    print('You are not eligible to drive')

numerator = 10
denominator = 20
if numerator == 0:
    print('result will always be 0')
elif numerator == denominator:
    print('result will always be 1')
elif denominator == 0:
    print('cannot divide by zero')
else:
    if denominator > numerator:
        print('result will be less than 1')
    print(f'Result = {numerator/denominator}')