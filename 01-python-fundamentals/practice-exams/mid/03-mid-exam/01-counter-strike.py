energy = int(input())
wins = 0

while True:
    distance = input()
    if distance == "End of battle":
        print(f"Won battles: {wins}. Energy left: {energy}")
        break
    
    distance = int(distance)

    if energy < distance:
        print(f"Not enough energy! Game ends with {wins} won battles and {energy} energy")
        break

    wins += 1
    energy -= distance
    if wins % 3 == 0:
        energy += wins