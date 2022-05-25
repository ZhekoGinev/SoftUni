from os import chdir, remove
from sys import path
chdir(path[0])

try:
    remove('my_first_file.txt')
except FileNotFoundError:
    print("File already deleted")