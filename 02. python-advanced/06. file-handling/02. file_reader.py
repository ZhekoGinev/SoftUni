from os import chdir
from sys import path
chdir(path[0])

with open('resources/File Reader/numbers.txt') as f:
    for i in f:
        print(i, end="")