import re

pattern = r"@#+[A-Z]{1}[a-zA-Z0-9]{4,}[A-Z]{1}@#+"

n = int(input())

for _ in range(n):
    data = input()
    match = re.match(pattern, data)
    if match is None: # if input does not match pattern
        print("Invalid barcode")
    else:
        code = "".join(i for i in match[0] if i.isdigit())
        if not code:  # if there are no digits set default to 00
            code = "00"
        print(f"Product group: {code}")
