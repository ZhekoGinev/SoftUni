import re

data = input()
word = input()

pattern = fr"\b{word}\b"

matches = re.findall(pattern, data, re.IGNORECASE)

print(len(matches))