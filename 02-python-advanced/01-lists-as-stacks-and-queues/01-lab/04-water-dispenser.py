water_qty = int(input())
queue = []

while True:
    command = input()
    if command == 'Start':
        break
    else:
        queue.append(command)


while True:
    command = input()
    if command == 'End':
        break
    else:
        command = command.split()
        if command[0] == 'refill':
            water_qty += int(command[1])
        else:
            liters = int(command[0])
            name = queue.pop(0)
            if water_qty >= liters:
                print(f"{name} got water")
                water_qty -= liters
            else:
                print(f"{name} must wait")


print(f"{water_qty} liters left")
