import os
import shutil

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

# Delete a directory
shutil.rmtree(f'{pwd}/data')