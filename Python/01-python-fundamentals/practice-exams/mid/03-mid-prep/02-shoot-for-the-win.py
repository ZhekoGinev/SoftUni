targets = [int(i) for i in input().split()]
count = 0

while True:
    command = input()
    if command == "End":
        break

    index = int(command)
    if index not in range(len(targets)):
        continue  # out of range

    for current_pos, target in enumerate(targets):
        if target == -1 or current_pos == index:
            continue # already shot or same target
        if target > targets[index]:
            targets[current_pos] -= targets[index]
        else:
            targets[current_pos] += targets[index]
    count += 1
    targets[index] = -1

print(f"Shot targets: {count} ->", end=" ")
print(*targets)