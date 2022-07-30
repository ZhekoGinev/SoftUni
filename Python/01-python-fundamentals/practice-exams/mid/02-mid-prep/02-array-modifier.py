numbers = [int(i) for i in input().split()]

while True:
    command = input()
    if command == "end":
        break

    if command == 'decrease':
        for num in range(len(numbers)):
            numbers[num] -= 1
    
    else:
        command = command.split()
        action = command[0]
        index1 = int(command[1])
        index2 = int(command[2])

        if action == "swap":
            numbers[index1], numbers[index2] = numbers[index2], numbers[index1]
        
        elif action == "multiply":
            numbers[index1] = numbers[index1] * numbers[index2]

print(*numbers, sep=', ')