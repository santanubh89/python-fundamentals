# Write a file
f = open('file.txt', 'w')
f.write('Writing from Python program\n')
f.write('Adding another line\n')
f.close()

# Read a file
f = open('file.txt', 'r')

content = f.read()
print(f'Content: {content}')

content = f.read()
print(f'Content blank after already read: {content}')

f.seek(0)
lines = f.readlines()
print(f'Lines: {lines}')
for line_no, content in enumerate(lines):
    print(f'Line {line_no}: {content}')
f.close()

# Read using with operator
with open('file.txt', 'a') as f:
    f.write('With operator does not need to call close\n')

# Append
f = open('file.txt', 'a')
f.write('Appending content in the file\n')

# Handling file not present
try:
    f = open('not_present.txt', 'r')
    print(f'Content: {f.read()}')
except FileNotFoundError:
    print('File not found')


# Write multiple lines
lines = ['Printing line 1 from python\n', 'This is line 2 from python\n']
f = open('file.txt', 'w')
f.writelines(lines)
print(type(f))

