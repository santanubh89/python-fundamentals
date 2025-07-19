from requests import HTTPError

def invoke_api_1(data):
    if data.isupper():
        raise HTTPError('request id must be lower case')
    print(f'API 1 executed successfully with request id {data}')

def invoke_api_2(data):
    print(f'API 2 executed successfully with request id {data}')

try:
    invoke_api_1('FOO')
except:
    print('API 1 failed to execute')
else:
    print('API 1 executed successfully')

try:
    invoke_api_1('FOO')
except HTTPError as e:
    print(f'API 1 failed to execute: {e}')
    invoke_api_2('FOO')
else:
    print('API 1 executed successfully')