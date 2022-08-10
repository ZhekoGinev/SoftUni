import re

data = input()

pattern = r"(([=/])([A-Z]{1}[a-zA-Z]{2,})(\2))"
destinations = []

matches = re.findall(pattern, data)

for m in matches:
    if m:
        destinations.append(m[2])

dest = ', '.join(destinations)
points = len(''.join(destinations))

print(f"Destinations: {dest}")
print(f"Travel Points: {points}")