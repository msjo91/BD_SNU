"""
Comma-Separated Values
A table expressing rows with 'newline' and columns with ',(comma)'
"""
import os
import csv

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
FILE_DIR1 = os.path.dirname(ROOT_DIR, 'fileIO_directory.txt')
FILE_DIR2 = os.path.join(ROOT_DIR, 'fileIO_directory2.txt')
with open(FILE_DIR1) as f:
    directory1 = f.read()
with open(FILE_DIR2) as f:
    directory2 = f.read()

with open(directory1) as csv_result_file:
    f_writer = csv.writer(csv_result_file)
    f_lst = ["bob", "kim", "mike"]
    f_writer.writerow(f_lst)

f_dict = {}
with open(directory2) as f:
    for line in f:
        # strip() removes newline
        row = line.strip().split(',')
    # Add dictionary as
    # Key : First word in the row
    # Value : Row without first word
    f_dict[row[0]] = row[1:]

f_dict2 = {}
with open(directory2, 'r+') as csv_data_file:
    f_reader = csv.reader(csv_data_file)
    for r in f_reader:
        row = r
        f_dict2[row[0]] = row[1:]
