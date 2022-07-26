import re

pattern = r"((www\.)([a-zA-Z0-9\-]+)(\.[a-z]+)+)"

res = []

line = input()

while True:
    if line:
        matches = re.search(pattern, line)
        if matches:
            res.append(matches.group(0))
        line = input()
    else:
        break

print('\n'.join(res))