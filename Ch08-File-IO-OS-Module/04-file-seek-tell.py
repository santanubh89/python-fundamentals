f = open('seek-tell-demo.txt', 'w')
f.write('This file will be used to demo Seek and Tell')
f.close()

f = open('seek-tell-demo.txt', 'r')
first_5 = f.read(5) # reads first n char
print(f'First 5 = {first_5}')
f.close()

f = open('seek-tell-demo.txt', 'r')
f.seek(10) # moves start char
current_start = f.tell()
print(f'Current start = {current_start}')
first_5 = f.read(5)
print(f'First 5 = {first_5}')
f.close()

with open('seek-tell-demo.txt', 'w') as f:
    f.write('Hello World')
    f.truncate(5)

with open('seek-tell-demo.txt', 'r') as f:
    print(f'Present content = {f.read()}')

