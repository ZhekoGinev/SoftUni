from os import chdir
from sys import path
chdir(path[0])

with open('my_first_file.txt', 'w') as f:
    f.write("There are no strings on me!")