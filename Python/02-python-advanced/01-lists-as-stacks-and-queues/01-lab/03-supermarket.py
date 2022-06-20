que = []

while True:
    command = input()
    if command == 'Paid':
        while len(que) > 0:
            print(que.pop(0))
    elif command == 'End':
        break
    else:
        que.append(command)

print(f"{len(que)} people remaining.")
