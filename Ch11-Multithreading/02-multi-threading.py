import time
import threading
from threading import Thread


def post_api_create(username):
    print(f'Execution Started:: {threading.current_thread().name}:: Username = {username}')
    time.sleep(1.5)
    print(f'Execution Finished:: {threading.current_thread().name}')
    return 'CreateResponse'

def get_api_read(username):
    print(f'Execution Started:: {threading.current_thread().name}:: Username = {username}')
    time.sleep(1.0)
    print(f'Execution Finished:: {threading.current_thread().name}')
    return 'ReadResponse'

def put_api_update(username, age):
    print(f'Execution Started:: {threading.current_thread().name}:: Username = {username}, age = {age}')
    time.sleep(2.0)
    print(f'Execution Finished:: {threading.current_thread().name}')

thread_create = threading.Thread(target=post_api_create, args=['Foo'], name='Thread_Create')
thread_read = threading.Thread(target=get_api_read, args=['Bar'], name='Thread_Read')
thread_update = threading.Thread(target=put_api_update, args=['Baz', 100], name='Thread_Update')

init = time.time()
thread_create.start()
thread_read.start()
thread_update.start()
print(f'Execution Started:: {time.time() - init}')

thread_create.join()
thread_read.join()
thread_update.join()
print(f'Execution Finished:: {time.time() - init}')

# post_api_create('Foo')
# get_api_read('Bar')
# put_api_update('Baz', 100)