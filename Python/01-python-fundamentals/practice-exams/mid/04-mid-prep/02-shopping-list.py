shopping_list = input().split("!")

while True:
    command = input()
    if command == "Go Shopping!":
        break
    tokens = command.split()
    action = tokens[0]
    item = tokens[1]
    new_item = tokens[-1]

    if action == "Urgent" and item not in shopping_list:
        shopping_list.insert(0, item)

    if item not in shopping_list:
        continue

    if action == "Unnecessary":
        shopping_list.remove(item)

    elif action == "Correct":
        shopping_list[shopping_list.index(item)] = new_item

    elif action == "Rearrange":
        shopping_list.append(shopping_list.pop(shopping_list.index(item)))

print(", ".join(shopping_list))
