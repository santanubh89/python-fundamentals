import requests


class APIInvocationError(Exception):
    def __init__(self, url, status, message):
        self.url = url
        self.status = status
        self.message = message
        super().__init__(self.message)
    def __str__(self):
        return f'HTTP {self.status}: {self.message}'

def invoke(url, params):
    if not url.startswith('https'):
        raise APIInvocationError(url, 400, 'Must use SSL')
    else:
        print('API executed successfully')

try:
    invoke('http://localhost:8000', {'id': 1})
except APIInvocationError as api_error:
    print(f'Error while invoking API: {api_error}')
finally:
    print('Closing connection')

try:
    invoke('https://localhost:8000', {'id': 1})
except APIInvocationError as api_error:
    print(f'Error while invoking API: {api_error.message}')
finally:
    print('Closing connection')