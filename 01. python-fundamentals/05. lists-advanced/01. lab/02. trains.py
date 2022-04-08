number_of_wagons = int(input())
train = [0] * number_of_wagons

while True:
    command = input()
    if command == "End":
        break
    inputs = command.split()
    command = inputs[0]
    if command == "add":
        number_of_passengers = int(inputs[1])
        train[-1] += number_of_passengers
    elif command == "insert":
        index = int(inputs[1])
        number_of_passengers = int(inputs[2])
        train[index] += number_of_passengers
    elif command == "leave":
        index = int(inputs[1])
        number_of_passengers = int(inputs[2])
        train[index] -= number_of_passengers

print(train)
