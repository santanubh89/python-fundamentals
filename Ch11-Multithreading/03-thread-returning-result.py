import time
import threading
from concurrent.futures.thread import ThreadPoolExecutor
from threading import Thread


def post_api_create(username):
    print(f'Execution Started:: POST - Create:: Username = {username}')
    time.sleep(1.5)
    print(f'Execution Finished:: POST - Create')
    return 'CreateResponse'

def get_api_read(username):
    print(f'Execution Started:: GET - Read:: Username = {username}')
    time.sleep(1.0)
    print(f'Execution Finished:: GET - Read')
    return 'ReadResponse'

def put_api_update(username, age):
    print(f'Execution Started:: PUT - Update:: Username = {username}, age = {age}')
    time.sleep(2.0)
    print(f'Execution Finished:: PUT - Update')

with ThreadPoolExecutor() as executor:
    future1 = executor.submit(post_api_create, 'Foo')
    future2 = executor.submit(get_api_read, 'Bar')
    future3 = executor.submit(put_api_update, 'Baz', 100)
    result1 = future1.result()  # This blocks until the function completes
    result2 = future2.result()  # This blocks until the function completes
    result3 = future3.result()  # This blocks until the function completes
    print('POST Response:', result1)
    print('GET Response:', result2)
    print('PUT Response:', result3)