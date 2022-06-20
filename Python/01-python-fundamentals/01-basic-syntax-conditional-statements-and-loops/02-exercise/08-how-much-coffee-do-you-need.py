events = ('cat', 'dog', 'coding', 'movie')
coffee_cups = 0

while True:
    command = input()
    if command == "END":
        break
    if command.lower() in events:
        if command.isupper():
            coffee_cups += 2
        elif command.islower():
            coffee_cups += 1

if coffee_cups > 5:
    print("You need extra sleep")
else:
    print(coffee_cups)
