number_of_rows = int(input())

# creates the battlefield and count all ships
battlefield = []
number_of_ships = 0

for row in range(number_of_rows):
    row = input().split()
    row = [int(i) for i in row]
    battlefield.append(row)

    for square in row:
        if square > 0:
            number_of_ships += 1

# creating the attack coordinates
attacked_squares = input().split()
attacked = [[int(i[0]), int(i[2])] for i in attacked_squares]

# executing the attacks
for attack in attacked:
    row = attack[0]
    col = attack[1]
    battlefield[row][col] -= 1

# counting the number of ships after the battle
number_of_ships_after = 0
for line in battlefield:
    for square in line:
        if square > 0:
            number_of_ships_after += 1

destroyed = abs(number_of_ships_after - number_of_ships)

print(destroyed)
