from re import findall
from functools import reduce

data = input()
pattern = r"((::|\*\*)([A-Z]{1}[a-z]{2,})(\2))"
matches = findall(pattern, data)
cool_threshold = reduce(lambda a, b: a * b, [int(n) for n in data if n.isdigit()])

print(f"Cool threshold: {cool_threshold}")
print(f"{len(matches)} emojis found in the text. The cool ones are:")
for m in matches:
    score = sum(ord(i) for i in m[2])
    if score > cool_threshold:
        print(m[0])
