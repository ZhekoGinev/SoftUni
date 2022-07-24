import re

data = input()

pattern = r"(^|(?<=\s))-?([0]|[1-9][0-9]*)(\.[0-9]+)?($|(?=\s))"

matches = re.finditer(pattern, data)

for m in matches:
    print(m.group(), end=" ")