data = list(input())
strings = ""
numbers = ""

for index, char in enumerate(data):
    if char.isdigit():
        numbers += char
        strings += " "
    else:
        strings += char.upper()
        numbers += " "

strings = strings.split()
numbers = numbers.split()

unique = len(set(''.join(strings)))

rage_message = ''.join(
    [f"{strings[i] * int(numbers[i])}"
    for i in range(len(strings))]
)

print(f"Unique symbols used: {unique}")
print(rage_message)