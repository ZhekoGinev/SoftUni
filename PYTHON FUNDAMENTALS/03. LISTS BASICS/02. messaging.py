numbers = input().split()
message = input()

# sum of all digints in the number
numbers = [sum([int(i) for i in num]) for num in numbers]

decoded = ""

for index in numbers:
    while index > len(message):  # if index is out of range
        index -= len(message)   # we continue counting from start

    # add the char at index number to decoded
    decoded += message[index]
    # remove the char from the original string
    message = message[:index] + message[index+1:]

print(decoded)
