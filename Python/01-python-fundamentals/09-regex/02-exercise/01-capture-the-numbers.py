import re

pattern = r"\d+"

line = input()

res = []

while True:
    if line:
        matches = re.findall(pattern, line)
        res += matches
        line = input()
    else:
        break

print(*res)