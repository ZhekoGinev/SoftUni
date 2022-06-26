targets = [int(i) for i in input().split()]

while True:
    command = input()
    if command == "End":
        break

    tokens = command.split()
    action = tokens[0]
    index = int(tokens[1])
    value = int(tokens[2])

    if action == "Shoot" and index in range(len(targets)):
        targets[index] -= value
        if targets[index] <= 0:
            targets.pop(index)

    elif action == "Add":
        if index not in range(len(targets)):
            print("Invalid placement!")
        else:
            targets.insert(index, value)

    elif action == "Strike":
        if (0 <= index - value) and (index + value < len(targets)):
            targets = targets[:index - value] + targets[index + value + 1:]
        else:
            print("Strike missed!")

print(*targets, sep="|")