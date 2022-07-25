import re

pattern = r"\d+"

line = input()

res = []

while True:
    if line:
        matches = re.findall(pattern, line)
        res += matches
    else:
        break
    line = input()

print(*res)