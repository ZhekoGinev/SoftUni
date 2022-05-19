number_of_cars = int(input())

parking = {}

for _ in range(number_of_cars):
    command = input().split()
    username = command[1]
    if command[0] == "register":
        license_plate = command[2]
        if username not in parking:
            parking[username] = license_plate
            print(f"{username} registered {license_plate} successfully")
        else:
            print(
                f"ERROR: already registered with plate number {license_plate}")
    elif command[0] == "unregister":
        if username not in parking:
            print(f"ERROR: user {username} not found")
        else:
            print(f"{username} unregistered successfully")
            del parking[username]

for user, plate in parking.items():
    print(f"{user} => {plate}")
