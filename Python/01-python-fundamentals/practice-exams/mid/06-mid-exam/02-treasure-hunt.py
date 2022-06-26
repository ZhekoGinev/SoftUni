chest = input().split("|")

while True:
    data = input()
    if data == "Yohoho!":
        break

    tokens = data.split()
    action = tokens[0]

    if action == "Loot":
        items = tokens[1:]
        for item in items:
            if item not in chest:
                chest.insert(0, item)

    elif action == "Drop":
        index = int(tokens[1])
        if 0 <= index < len(chest):
            chest.append(chest.pop(index))

    elif action == "Steal":
        count = int(tokens[1])
        booty = []
        for i in range(count):
            if len(chest) > 0:
                booty.insert(0, chest.pop())
            else:
                break

        if len(booty) > 0:
            print(*booty, sep=", ")


if chest:
    avg = sum(len(i) for i in chest) / len(chest)
    print(f"Average treasure gain: {avg:.2f} pirate credits.")
else:
    print("Failed treasure hunt.")
