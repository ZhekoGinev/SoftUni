energy = int(input())
wins = 0
lost_game = False

while True:
    distance = input()
    if distance == "End of battle":
        break
    
    distance = int(distance)

    if energy >= distance:
        wins += 1
        energy -= distance
    else:
        lost_game = True
        print(f"Not enough energy! Game ends with {wins} won battles and {energy} energy")
        break
    
    if wins % 3 == 0:
        energy += wins

if not lost_game:
    print(f"Won battles: {wins}. Energy left: {energy}")