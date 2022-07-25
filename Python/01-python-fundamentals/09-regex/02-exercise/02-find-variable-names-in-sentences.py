import re

data = input()

pattern = r"\b_([a-zA-Z0-9]+)\b" 
# \b_([a-zA-Z]+[0-9]*)\b would be a bit more accurate
# because a variable name cannot start with a number
matches = re.findall(pattern, data)

print(','.join(matches))