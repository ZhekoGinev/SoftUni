import re

data = input()

pattern = r"\b(\d{2})([.\-/])([A-Z]{1}[a-z]{2})\2(\d{4})\b"

matches = re.findall(pattern, data)

for m in matches:
    print(f"Day: {m[0]}, Month: {m[2]}, Year: {m[3]}")