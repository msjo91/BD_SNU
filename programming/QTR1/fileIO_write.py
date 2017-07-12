import os

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
FILE_DIR = os.path.join(ROOT_DIR, 'fileIO_directory.txt')
with open(FILE_DIR) as f:
    directory = f.read()

f = open(directory, 'w')

# Overwrite data
for i in range(1, 11):
    data = "{}\n".format(i)
    f.write(data)

# Add data
for i in range(11, 20):
    data = "{}\n".format(i)
    f.write(data)

f.close()
