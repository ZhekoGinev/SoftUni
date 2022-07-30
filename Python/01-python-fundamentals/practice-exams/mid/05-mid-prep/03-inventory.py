inventory = input().split(", ")

while True:
    command = input()
    if command == "Craft!":
        break
    tokens = command.split(" - ")
    action = tokens[0]
    item = tokens[1]
    if action == "Collect" and item not in inventory:
        inventory.append(item)
    elif action == "Drop" and item in inventory:
        inventory.remove(item)
    elif action == "Combine Items":
        items = item.split(":")
        old_item = items[0]
        new_item = items[1]
        if old_item in inventory:
            inventory.insert(inventory.index(old_item) + 1, new_item)
    elif action == "Renew":
        if item in inventory:
            inventory.append(item)
            inventory.remove(item)

inventory = ", ".join(inventory)
print(inventory)
