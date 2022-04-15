import os, sys
os.chdir(sys.path[0])

file = os.path.exists('resources/File Opener/text.txt')
if file:
    print("File found")
else:
    print("File not found")
