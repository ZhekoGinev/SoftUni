message = input()

numbers = [int(n) for n in message if n.isdigit()]
characters = [c for c in message if not c.isdigit()]

take = [n for i, n in enumerate(numbers) if i % 2 == 0]
skip = [n for i, n in enumerate(numbers) if i % 2 != 0]

characters = "".join(characters)
decoded = ""

for index in range(len(take)):
    decoded += characters[:take[index]]
    characters = characters[take[index] + skip[index]:]

print(decoded)
