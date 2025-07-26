import os
import shutil
import time

f = open('data.txt', 'w')
f.write('This is OS Module demo')
f.close()

pwd = os.getcwd()
f = open(f'{pwd}/data.txt', 'r')
content = f.read()
print(content)

# Copy file
shutil.copy(f'{pwd}/data.txt', f'{pwd}/data')
print('File copied successfully')

for folder, subfolders, files in os.walk(f'{pwd}/data'):
    print(f'Folder = {folder}')
    print(f'Subfolders = {subfolders}')
    print(f'Files = {files}')

# Remove a directory
shutil.rmtree(f'{pwd}/test_dir')
print(f'Removed test_dir')
time.sleep(5)

# Copy a directory
shutil.copytree(f'{pwd}/test_dir_bk', f'{pwd}/test_dir')
print('File copied successfully')
