import re

data = input()

pattern = r"[@#]+([a-z]{3,})[@#]+\W*/+(\d+)/+"

matches = re.findall(pattern, data)

for m in matches:
    print(f"You found {m[1]} {m[0]} eggs!")