MAX_HP = 100
hp = MAX_HP
btc = 0
room_n = 0
success = True

rooms = input().split("|")

for room in rooms:
    tokens = room.split()
    command = tokens[0]
    value = int(tokens[1])
    room_n += 1

    if command == "potion":
        deficit = MAX_HP - hp
        if deficit > value:
            hp += value
            print(f"You healed for {value} hp.")
            print(f"Current health: {hp} hp.")
        else:
            hp = 100
            amount = deficit
            print(f"You healed for {amount} hp.")
            print(f"Current health: {hp} hp.")
    elif command == "chest":
        btc += value
        print(f"You found {value} bitcoins.")
    else:
        hp -= value
        if hp > 0:
            print(f"You slayed {command}.")
        else:
            print(f"You died! Killed by {command}.")
            print(f"Best room: {room_n}")
            success = False
            break

if success:
    print("You've made it!")
    print(f"Bitcoins: {btc}")
    print(f"Health: {hp}")
