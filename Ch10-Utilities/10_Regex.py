import re

PATTERN_PHONE_NO = r'(\d\d\d)-\d\d\d-\d\d\d\d'
input_phone_no = '408-555-1234'

input_text = "The agent's phone number is 408-555-1234"
pattern = 'phone'
match_result = re.search(pattern, input_text)
print(f'Match result: {match_result}')
if match_result:
    print(f'The word phone is present in position => {match_result.span()}')
else:
    print(f'The given pattern is not present in the input')

# multiple matches
input_text = "My phone once, my phone twice"
match_list = re.findall(pattern, input_text)
print(f'Match result: {match_list}')

for match in re.finditer(pattern, input_text):
    print(f'Match result present in: {match.span()}')

input_text = 'My current phone number is 1234567890. Previous phone number was 9876543210, which I dont have anymore.'
PATTERN_PHONE_NO = r'\d\d\d\d\d\d\d\d\d\d'
match_list = re.findall(PATTERN_PHONE_NO, input_text)
print(f'All phone numbers: {match_list}')

PATTERN_PHONE_NO = r'\d{10}'
match_list = re.findall(PATTERN_PHONE_NO, input_text)
print(f'All phone numbers: {match_list}')

input_text = 'My current phone number is 123-456-7890. Previous phone number was 987-654-3210, which I dont have anymore.'
PATTERN_PHONE_NO = r'\d{3}-\d{3}-\d{4}'
match_list = re.findall(PATTERN_PHONE_NO, input_text)
print(f'All phone numbers: {match_list}')

input_text = 'My current phone number is 123-456-7890.'
PATTERN_PHONE_NO = r'(\d{3})-(\d{3})-(\d{4})'
match_list = re.search(PATTERN_PHONE_NO, input_text)
print(f'All phone numbers: {match_list.group()}')
print(f'Country code = {match_list.group(1)}')

PATTERN_PHONE_NO = '' # 1234567890
PATTERN_PHONE_NO_HYPHENATED = '' # 123-456-7890
PATTERN_PHONE_NO_COUNTRY_CODE = '' # 91-1234567890
PATTERN_EMAIL_ID = '' # user@gmail.com
PATTERN_PAN_NO = '' # ABCDE1234F
PATTERN_AADHAAR_NO = '' # 1234-5678-9012
PATTERN_PASSPORT_NO = '' # A12345678

# or operator
print(re.search(r'cat|dog', 'There is a cat in our room')) # span=(11, 14), match='cat'
print(re.search(r'cat|dog', 'This dog is a husky')) # span=(5, 8), match='dog'
print(re.search(r'cat|dog', 'Elephant is a big animal')) # None

# wildcard operator
print(re.findall(r'.at', 'The cat sat there wearing a hat')) # ['cat', 'sat', 'hat']
print(re.findall(r'...at', 'The cat sat there wearing a hat and went to splat')) # ['e cat', 'a hat', 'splat']

print(re.search(r'^\d', '1 is a number')) # searches if the text starting with a number
print(re.search(r'\d$', 'roll no is 202')) # searches if the text ending with a number

# remove all numbers
phrase = 'There are 3 numbers 34 inside 5 in this sentence'
pattern = r'[^\d]+'
match_result = re.findall(pattern, phrase)
print(f'Non numeric parts: {match_result}')

# remove all special characters
phrase = 'This is a string! but it has punctuations. How can we remove it?'
pattern = r'[^!.? ]+'
match_result = re.findall(pattern, phrase)
print(f'Non numeric parts: {' '.join(match_result)}')