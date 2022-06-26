numbers = input().split()
message = input()

numbers = [sum([int(i) for i in num]) for num in numbers]
decoded = ""

for index in numbers:
    while index > len(message):
        index -= len(message)

    decoded += message[index]
    message = message[:index] + message[index + 1 :]

print(decoded)
