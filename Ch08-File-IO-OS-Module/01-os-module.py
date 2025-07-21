f = open('data.txt', 'w')
f.write('This is OS Module demo')
f.close()

import os

# Create directory
if not os.path.exists('data'):
    os.mkdir('data')

for i in range(0, 5):
    os.mkdir(f'data/day_{i+1}')

# Rename
for i in range(0, 5):
    os.rename(f'data/day_{i+1}', f'data/content_{i+1}')

# Current working directory
pwd = os.getcwd()
print(f'Current working directory: {pwd}')

# List folders in directory
folders = os.listdir(f'{pwd}/data')
print(f'Folders: {folders}')

# Delete a file
os.unlink(f'{pwd}/data.txt')

# Delete a directory
os.rmdir(f'{pwd}/data/content_1')