name = 'FooBarBaz'
phone_no = '9876543210'
space = '   '

print(f'Alpha Numeric-- Name: {name.isalnum()}, Phone: {phone_no.isalnum()}, Space: {space.isalnum()}')
print(f'Alphabetic-- Name: {name.isalpha()}, Phone: {phone_no.isalpha()}, Space: {space.isalpha()}')
print(f'Decimal-- Name: {name.isdecimal()}, Phone: {phone_no.isdecimal()}, Space: {space.isdecimal()}')
print(f'Digit-- Name: {name.isdigit()}, Phone: {phone_no.isdigit()}, Space: {space.isdigit()}')
print(f'Numeric-- Name: {name.isnumeric()}, Phone: {phone_no.isnumeric()}, Space: {space.isnumeric()}')
print(f'Space-- Name: {name.isspace()}, Phone: {phone_no.isspace()}, Space: {space.isspace()}')

message = '@@Hello World!'
print(f'Starts with @: {message.startswith("@")}, Ends with !: {message.endswith("!")}')

# contains check
if 'Hello' in message:
    print('Greeting message!')