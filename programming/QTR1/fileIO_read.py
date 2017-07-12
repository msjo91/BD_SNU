import os

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
FILE_DIR = os.path.join(ROOT_DIR, 'fileIO_directory.txt')
with open(FILE_DIR) as f:
    directory = f.read()

f = open(directory, 'r')

# Print a single line
line = f.readline()
print(line)

# Print every line
while True:
    line = f.readline()
    if not line:
        break
    print(line)

# Print every line in a list
lines = f.readlines()
print(lines)

# Print every line as string
data = f.read()
print(data)

f.close()

"""
Note : rstrip(), lstrip(), strip()
"""
