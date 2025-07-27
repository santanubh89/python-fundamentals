import concurrent
import multiprocessing
import time
from random import random


def post_api_create(username):
    print(f'Execution Started:: Create:: Username = {username}')
    time.sleep(2)
    print(f'Execution Finished:: Create:: Username = {username}')
    return f'CreateResponse for {username}'

users = ['Foo', 'Bar', 'Baz']

if __name__ == '__main__':
    processes = []
    for user in users:
        p = multiprocessing.Process(target=post_api_create, args=[user])
        p.start()
        processes.append(p)
    for p in processes:
        p.join()

from concurrent.futures import ProcessPoolExecutor

if __name__ == '__main__':
    with ProcessPoolExecutor() as executor:
        l = [f'User{i}' for i in range(3)]
        results = executor.map(post_api_create, l)
        for result in results:
            print(result)