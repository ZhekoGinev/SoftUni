# I did not optimize the solution because it will decrease readability
pirates = [int(i) for i in input().split(">")]
warship = [int(i) for i in input().split(">")]
MAX_HP = int(input())
victory = None

while True:
    command = input()
    if command == "Retire":
        break
    command, *tokens = command.split()

    if victory == False:
        continue

    if command == "Fire":
        index = int(tokens[0])
        damage = int(tokens[1])
        if 0 <= index < len(warship):
            warship[index] -= damage
            if warship[index] <= 0:
                print("You won! The enemy ship has sunken.")
                victory = True
                break
    
    elif command == "Defend":
        start = int(tokens[0])
        end = int(tokens[1])
        damage = int(tokens[2])
        if 0 <= start <= end and end < len(pirates):
            for section in range(start, end + 1):
                pirates[section] -= damage
                if pirates[section] <= 0:
                    print("You lost! The pirate ship has sunken.")
                    victory = False
                    break

    elif command == "Repair":
        index = int(tokens[0])
        hp = int(tokens[1])
        if 0 <= index < len(pirates):
            pirates[index] += hp
            if pirates[index] > MAX_HP:
                pirates[index] = MAX_HP
    
    elif command == "Status":
        critical = len([s for s in pirates if s < MAX_HP * 0.2])
        print(f"{critical} sections need repair.")

pirates_hp = sum(pirates)
warship_hp = sum(warship)

if victory is None:
    print(f"Pirate ship status: {pirates_hp}")
    print(f"Warship status: {warship_hp}")