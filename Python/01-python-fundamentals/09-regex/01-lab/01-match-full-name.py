import re

data = input()

pattern = r"\b[A-Z]{1}[a-z]+ [A-Z]{1}[a-z]+\b"

res = re.findall(pattern, data)
print(" ".join(res))
