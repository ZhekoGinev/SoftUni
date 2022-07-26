import re

pattern = r"(?<=\s)([a-z0-9]+[a-z0-9\.\-\_]*@[a-z\-]+(\.[a-z]+)+)"

data = input()

matches = re.findall(pattern, data)

for m in matches:
    print(m[0])