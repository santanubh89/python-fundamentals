import time

def loop_while():
    i = 0
    while i < 500000:
        i = i + 1


def loop_for():
    for i in range(500000):
        pass


init = time.time()
loop_while()
elapsed = (time.time() - init) * 1000
print(f'While loop: {elapsed:.3f} milliseconds')

init = time.time()
loop_for()
elapsed = (time.time() - init) * 1000
print(f'For loop: {elapsed:.3f} milliseconds')
