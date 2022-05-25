number_of_wagons = int(input())
train = [0] * number_of_wagons

while True:
    command = input()
    if command == "End":
        break
    tokens = command.split()
    command = tokens[0]
    if command == "add":
        number_of_passengers = int(tokens[1])
        train[-1] += number_of_passengers
    elif command == "insert":
        index = int(tokens[1])
        number_of_passengers = int(tokens[2])
        train[index] += number_of_passengers
    elif command == "leave":
        index = int(tokens[1])
        number_of_passengers = int(tokens[2])
        train[index] -= number_of_passengers

print(train)
