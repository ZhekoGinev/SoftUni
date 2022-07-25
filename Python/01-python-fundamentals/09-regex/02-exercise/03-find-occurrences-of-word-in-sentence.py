import re

data = input()
word = input()

pattern = r"\b" + word + r"\b"

matches = re.findall(pattern, data, re.IGNORECASE)

print(len(matches))